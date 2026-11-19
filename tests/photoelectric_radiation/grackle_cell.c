#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "grackle.h"

/* Matched scalar/per-cell Habing inputs through real Grackle APIs. */

int main(int argc, char **argv)
{
  if (argc != 4) return 2;
  chemistry_data chemistry;
  if (!local_initialize_chemistry_parameters(&chemistry)) return 2;
  chemistry_data_storage rates = {0};
  code_units units = {0};
  grackle_field_data fields = {0};
  chemistry.use_grackle = 1;
  chemistry.use_isrf_field = atoi(argv[3]);
  chemistry.primordial_chemistry = 2;
  chemistry.metal_cooling = 1;
  chemistry.dust_chemistry = 1;
  chemistry.photoelectric_heating = 0;
  chemistry.cmb_temperature_floor = 0;
  chemistry.UVbackground = 0;
  chemistry.grackle_data_file = argv[1];
  chemistry.h2_on_dust = 1;
  chemistry.use_dust_density_field = 1;
  const double metallicity = 0.00054;
  double T,nH,xe,G,dust_ratio;
  double factor=pow(10.,atoi(argv[2]));
  units.density_units = 1.67262171e-24*factor;
  units.length_units = 1.e18*factor;
  units.time_units = 1.e13*sqrt(factor);
  units.velocity_units = units.length_units/units.time_units;
  units.a_units = units.a_value = 1.0;
  if (!local_initialize_chemistry_data(&chemistry, &rates, &units)) return 3;
  int dim[3] = {1,1,1}, begin[3] = {0,0,0}, end[3] = {0,0,0};
  fields.grid_rank = 1;
  fields.grid_dimension = dim; fields.grid_start = begin; fields.grid_end = end;
  fields.grid_dx = 1.0;
  while(scanf("%lf %lf %lf %lf %lf", &T,&nH,&xe,&G,&dust_ratio)==5){
  chemistry.interstellar_radiation_field = chemistry.use_isrf_field ? 999.0 : G;
  gr_float local_isrf = G;
  fields.isrf_habing = chemistry.use_isrf_field ? &local_isrf : NULL;
  gr_float rho=nH/0.76/factor, hi=nH*(1-xe)/factor, hii=nH*xe/factor, hm=1.e-40;
  gr_float hei=rho*.24, heii=1.e-40, heiii=1.e-40;
  gr_float h2=1.e-40,h2ii=1.e-40,electron=nH*xe/factor;
  gr_float metal=rho*metallicity,dust=rho*dust_ratio;
  gr_float energy=T*1.3806504e-16/(1.67262171e-24*(chemistry.Gamma-1.))*(0.76*(1+xe)+0.24/4.+metallicity/16.)/pow(units.velocity_units,2);
  gr_float vx = 0., vy = 0., vz = 0.;
  fields.density = &rho; fields.HI_density = &hi; fields.HII_density = &hii;
  fields.HM_density = &hm; fields.HeI_density = &hei;
  fields.HeII_density = &heii; fields.HeIII_density = &heiii;
  fields.H2I_density = &h2; fields.H2II_density = &h2ii;
  fields.e_density = &electron; fields.metal_density = &metal;
  fields.dust_density = &dust; fields.internal_energy = &energy;
  fields.x_velocity = &vx; fields.y_velocity = &vy; fields.z_velocity = &vz;
  gr_float cooling_time = 0.;
  if (!local_calculate_cooling_time(&chemistry, &rates, &units,
                                    &fields, &cooling_time)) return 4;
  gr_float actual_T=0;
  if (!local_calculate_temperature(&chemistry,&rates,&units,&fields,&actual_T)) return 9;
  // Exercise both public consumers of the radiation field.
  if (!local_solve_chemistry(&chemistry, &rates, &units, &fields,
                            .01*fabs((double)cooling_time))) return 10;
  printf("RESULT");
  printf(" %.17g %.17g %.17g\n",(double)cooling_time*units.time_units,(double)actual_T,(double)energy*pow(units.velocity_units,2));
  }
  if (!local_free_chemistry_data(&chemistry, &rates)) return 8;
  return 0;
}

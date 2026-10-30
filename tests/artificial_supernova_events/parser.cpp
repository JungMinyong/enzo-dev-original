#include "../../src/enzo/ArtificialSupernovaTable.h"
#include <cassert>
#include <cstdio>

void write(const char *path, const char *text)
{
  std::ofstream f(path);
  f << text;
}

int main(int argc, char **argv)
{
  assert(argc == 2);
  const char *path = argv[1];
  write(path, "# time_Myr x y z\n0.1 .5 .5 .5\n0.1 .6 .4 .5 # simultaneous\n.2 .5 .5 .4\n");
  artificial_sn::Table table = artificial_sn::read(path);
  assert(table.events.size() == 3);
  assert(table.events[1].time_myr == .1);
  assert(table.events[1].position[0] == .6);
  assert(table.fingerprint == artificial_sn::read(path).fingerprint);
  write(path, ".1 .5 .5 .5\n");
  assert(table.fingerprint != artificial_sn::read(path).fingerprint);
  const char *bad[] = {"", "# comments only\n", "0 .5 .5 .5\n",
    "-1 .5 .5 .5\n", ".1 .5 .5\n", ".1 .5 .5 .5 extra\n",
    ".2 .5 .5 .5\n.1 .5 .5 .5\n", "nan .5 .5 .5\n",
    ".1 inf .5 .5\n", "1e400 .5 .5 .5\n"};
  for (unsigned i = 0; i < sizeof(bad)/sizeof(bad[0]); ++i) {
    write(path, bad[i]);
    bool rejected = false;
    try { artificial_sn::read(path); }
    catch (const std::runtime_error &) { rejected = true; }
    assert(rejected);
  }
  std::remove(path);
  bool rejected = false;
  try { artificial_sn::read(path); }
  catch (const std::runtime_error &) { rejected = true; }
  assert(rejected);
  puts("SN parser tests passed.");
}

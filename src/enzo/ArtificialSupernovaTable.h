#ifndef ARTIFICIAL_SUPERNOVA_TABLE_H
#define ARTIFICIAL_SUPERNOVA_TABLE_H

// Include before Enzo's precision macros. This parser is independent of Enzo.
#include <cmath>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <stdint.h>
#include <climits>

namespace artificial_sn {
struct Event {
  double time_myr;
  double position[3];
};

struct Table {
  std::vector<Event> events;
  std::string fingerprint;
};

inline Table read(const char *filename)
{
  std::ifstream input(filename, std::ios::binary);
  if (!input) throw std::runtime_error("Cannot open artificial SN event file.");
  Table table;
  uint64_t hash = UINT64_C(14695981039346656037);
  std::string line;
  unsigned long line_number = 0;
  while (std::getline(input, line)) {
    ++line_number;
    for (std::string::size_type j = 0; j < line.size(); ++j) {
      hash ^= static_cast<unsigned char>(line[j]);
      hash *= UINT64_C(1099511628211);
    }
    if (!input.eof()) {
      hash ^= static_cast<unsigned char>('\n');
      hash *= UINT64_C(1099511628211);
    }
    std::istringstream row(line.substr(0, line.find('#')));
    row >> std::ws;
    if (row.eof()) continue;
    Event event;
    std::string extra;
    if (!(row >> event.time_myr >> event.position[0] >>
          event.position[1] >> event.position[2]) || (row >> extra))
      throw std::runtime_error("Expected time_Myr x y z at SN file line " +
                               std::to_string(line_number));
    if (!std::isfinite(event.time_myr) || event.time_myr <= 0)
      throw std::runtime_error("SN times must be finite and positive.");
    for (unsigned j = 0; j < 3; ++j)
      if (!std::isfinite(event.position[j]))
        throw std::runtime_error("SN positions must be finite.");
    if (!table.events.empty() &&
        event.time_myr < table.events.back().time_myr)
      throw std::runtime_error("SN times must be in nondecreasing order.");
    if (table.events.size() >= static_cast<unsigned>(INT_MAX / 4))
      throw std::runtime_error("Too many artificial SN events.");
    table.events.push_back(event);
  }
  if (input.bad()) throw std::runtime_error("Error reading SN event file.");
  if (table.events.empty()) throw std::runtime_error("SN event file is empty.");
  std::ostringstream hex;
  hex << std::hex << std::setfill('0') << std::setw(16) << hash;
  table.fingerprint = hex.str();
  return table;
}
}
#endif

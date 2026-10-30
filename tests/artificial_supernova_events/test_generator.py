import importlib.util
import math
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[2] / "run/generate_artificial_sn_events.py"
spec = importlib.util.spec_from_file_location("sn_generator", path)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class GeneratorTest(unittest.TestCase):
    def sample(self, seed=13, sampling="periodic"):
        return generator.generate(seed, 5, 4e-7, 59000, 250, 100,
                                  (.5, .5, .5), sampling)

    def test_periodic_and_reproducible(self):
        rows = self.sample()
        self.assertEqual([r[0] for r in rows], [2.5, 5])
        self.assertEqual(rows, self.sample())
        self.assertNotEqual(rows, self.sample(seed=14))

    def test_poisson_and_geometry(self):
        rows = generator.generate(42, 100, 4e-6, 59000, 250, 100,
                                  (.5, .5, .5), "poisson")
        self.assertTrue(all(a[0] < b[0] for a, b in zip(rows, rows[1:])))
        for t, x, y, z in rows:
            self.assertLessEqual(math.hypot(x-.5, y-.5)*59000, 250)
            self.assertLessEqual(abs(z-.5)*59000, 100)
            self.assertGreater(t, 0)
            self.assertLessEqual(t, 100)

    def test_bad_arguments(self):
        for rate in [0, -1, float("nan")]:
            with self.assertRaises(ValueError):
                generator.generate(1, 5, rate, 59000, 250, 100, (.5, .5, .5))
        with self.assertRaises(ValueError):
            generator.generate(1, 5, 4e-7, 100, 250, 100, (.5, .5, .5))


if __name__ == "__main__":
    unittest.main()

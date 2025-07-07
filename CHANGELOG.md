# 📦 Changelog

All notable changes to this project will be documented in this file.

Format follows [Semantic Versioning](https://semver.org/).

---

## [v1.1.0] - 2025-07-07
### Added
- Load tickers from external configuration file (e.g., `config/config.json`).
- Implemented `--loop` flag to run the script automatically every 24 hours.
- CSV files are now saved in the `exports/` folder with timestamped filenames.
- Investment Disclaimer added to `README.md`.

### Changed
- Dependency management improved using `pip-tools` (`requirements.in` / `requirements.txt`).
- Updated usage instructions in `README.md`, including automation tips (cron/Task Scheduler).

### Fixed
- Prevented script crash when passing invalid or unsupported ticker symbols (e.g., `"LHA"` without `.DE`).


---

## [v1.0.1] - 2025-06-19
### Changed
- Updated `README.md` with license info, Python version, and badge.


---

## [v1.0.0] - 2025-06-19
### Added
- Initial stable release.
- Support for S&P 500 tickers.
- Indicators: dividend yield, payout ratio, FCF, CAGR (1Y–10Y).
- Data export to `dividend_data.csv`.

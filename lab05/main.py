from logstats import count_levels, top_errors, format_report

def main():
    filename = input().strip()

    total_parsed = 0
    error_count = 0
    broken_count = 0

    with open(filename, encoding="utf-8") as log:
        for line in log:
            line = line.strip()
            if not line:
                continue

            total_parsed += 1
            parts = line.split(" ", 2)

            if len(parts) == 3 and parts[1] in {"DEBUG", "INFO", "WARNING", "ERROR"}:
                if parts[1] == "ERROR":
                    error_count += 1
            else:
                broken_count += 1

    print(total_parsed)
    print(error_count)
    print(broken_count)

    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(filename, encoding="utf-8") as log:
        top_errs = top_errors(log, 3)

    report_text = format_report(counts, top_errs)

    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report_text)

if __name__ == "__main__":
    main()

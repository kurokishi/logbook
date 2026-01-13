from datetime import date
import calendar


def resolve_period(period_type, year, period_value):
if period_type == "monthly":
start = date(year, period_value, 1)
end = date(year, period_value, calendar.monthrange(year, period_value)[1])
label = start.strftime("%B %Y")
elif period_type == "quarterly":
sm = (period_value - 1) * 3 + 1
em = sm + 2
start = date(year, sm, 1)
end = date(year, em, calendar.monthrange(year, em)[1])
label = f"Triwulan {period_value} {year}"
elif period_type == "semester":
sm, em = (1, 6) if period_value == 1 else (7, 12)
start = date(year, sm, 1)
end = date(year, em, calendar.monthrange(year, em)[1])
label = f"Semester {period_value} {year}"
else:
raise ValueError("Invalid period")
return start, end, label

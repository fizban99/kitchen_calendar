import os, sys
from tempfile import gettempdir
from photocalendar import PhotoCalendar


# directories to be used. If you want to build your own calendar, you can use the same directory structure
# buildDirectory            = os.path.join(gettempdir(),"photocalendar-example2")   # main build directory
buildDirectory = os.path.join(os.curdir, "kitchen_calendar")
dataDirectory             = os.path.join(buildDirectory,"data")                   # where auxiliary data will be put ...
title                     = "2023"                                  # ... title
notesFile                 = os.path.join(dataDirectory,"notes.dat")               # ... or notes for days
nameDaysFile              = os.path.join(dataDirectory,"nameDays.dat")            # ... or name-days
religiousHolidaysFile     = os.path.join(dataDirectory,"religiousHolidays.dat")   # ... or religious holidays
publicHolidaysFile        = os.path.join(dataDirectory,"publicHolidays.dat")      # ... or public holidays
weekDayNamesFile          = os.path.join(dataDirectory,"weekDayNames.dat")        # ... or custom names of week days
abbrWeekDayNamesFile      = os.path.join(dataDirectory,"abbrWeekDayNames.dat")    # ... or custom abbreviations of weekday names
monthNamesFile            = os.path.join(dataDirectory,"monthNames.dat")          # ... or custom names of months
abbrMonthNamesFile        = os.path.join(dataDirectory,"abbrMonthNames.dat")      # ... or custom abbreviations of month names
template                  = os.path.join(os.curdir,"kitchen")


# create the calendar and save it
calendar = PhotoCalendar(
	outputBase                = os.path.join(buildDirectory,"kitchen_calendar"),
	year                      = 2023,
	firstWeekDay              = "Mo",
	title                     = title,
	nameDaysFile              = nameDaysFile,
	religiousHolidaysFile     = religiousHolidaysFile,
	publicHolidaysFile        = publicHolidaysFile,
	notesFile                 = notesFile,
	weekDayNamesFile          = weekDayNamesFile,
	abbrWeekDayNamesFile      = abbrWeekDayNamesFile,
	monthNamesFile            = monthNamesFile,
	abbrMonthNamesFile        = abbrMonthNamesFile,
	template                  = template,
)
calendar.toHTML()

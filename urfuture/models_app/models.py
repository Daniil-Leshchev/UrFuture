# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Professions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    knowledge = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'professions'


class Competencies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'competencies'


class Courses(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    knowledge = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    discipline_id = models.BigIntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    direction_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'courses'


class Disciplines(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplines'


class Directions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'directions'


class DisciplinesDirections(models.Model):
    id = models.BigAutoField(primary_key=True)
    discipline = models.ForeignKey(Disciplines, models.DO_NOTHING)
    direction = models.ForeignKey(Directions, models.DO_NOTHING, blank=True, null=True)
    semester = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'disciplines-directions'


class ProfessionCompetencyCourseLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    profession = models.ForeignKey('Professions', models.DO_NOTHING)
    competency = models.ForeignKey(Competencies, models.DO_NOTHING)
    course = models.ForeignKey(Courses, models.DO_NOTHING)
    weight = models.IntegerField()
    discipline = models.ForeignKey(Disciplines, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profession_competency_course_links'

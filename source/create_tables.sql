--java -jar schemaspy-6.1.0.jar -configFile schema_spy.properties

BEGIN;

CREATE SCHEMA bioacustica;

CREATE TABLE bioacustica."case"
(
    id_case smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_case)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.catalogue
(
    id_catalogue serial NOT NULL,
    id_sampling smallint NOT NULL,
    id_country smallint NOT NULL,
    id_department smallint NOT NULL,
    id_municipality smallint NOT NULL,
    id_vereda smallint NOT NULL,
    id_locality smallint NOT NULL,
    id_gain smallint NOT NULL,
    id_filter smallint NOT NULL,
    id_collector smallint NOT NULL,
    id_h_serial smallint NOT NULL,
    id_supply smallint NOT NULL,
    id_case smallint NOT NULL,
    id_memory smallint NOT NULL,
    id_habitat smallint NOT NULL,
    id_precision smallint NOT NULL,
    id_datum smallint NOT NULL,
    id_microphone smallint NOT NULL,
    elevation integer,
    height integer,
    chunks smallint,
    size real,
    latitude real,
    longitude real,
    description character varying(100),
    PRIMARY KEY (id_catalogue)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.catalogue_obs
(
    id_catalogue_obs serial NOT NULL,
    id_catalogue integer NOT NULL,
    observation character varying(100),
    PRIMARY KEY (id_catalogue_obs)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.datum
(
    id_datum smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_datum)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.evidence
(
    id_evidence smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_evidence)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.format
(
    id_format smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_format)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.funding
(
    id_funding smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_funding)
)
WITH (
    OIDS = FALSE
);


COMMENT ON TABLE bioacustica.funding
    IS 'ESTA TABLA SIRVE PARA X COSA modificado';

COMMENT ON COLUMN bioacustica.funding.id_funding
    IS 'ID Auto incremental';

CREATE TABLE bioacustica.h_serial
(
    id_h_serial smallserial NOT NULL,
    id_hardware smallint NOT NULL,
    h_serial character varying(64),
    PRIMARY KEY (id_h_serial)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.habitat
(
    id_habitat smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_habitat)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.hardware
(
    id_hardware smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_hardware)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.label
(
    id_label smallserial NOT NULL,
    id_type smallint NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_label)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.labeled
(
    id_labeled serial NOT NULL,
    id_label smallint NOT NULL,
    id_record integer NOT NULL,
    id_evidence smallint NOT NULL,
    id_labeler smallint NOT NULL,
    id_software smallint NOT NULL,
    id_measure smallint NOT NULL,
    date timestamp with time zone NOT NULL,
    membership numeric(4),
    n_calls smallint,
    id_pulse_type smallint,
    id_time_detail integer,
    id_frequency_detail integer,
    PRIMARY KEY (id_labeled)
)
WITH (
    OIDS = FALSE
);

COMMENT ON COLUMN bioacustica.labeled.date
    IS 'Fecha de etiquetado';

CREATE TABLE bioacustica.memory
(
    id_memory smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_memory)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.photo_path
(
    id_photo_path serial NOT NULL,
    id_catalogue integer NOT NULL,
    path character varying(100),
    PRIMARY KEY (id_photo_path)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica."precision"
(
    id_precision smallserial NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_precision)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.project
(
    id_project smallserial NOT NULL,
    id_funding smallint NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_project)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.record
(
    id_record serial NOT NULL,
    id_catalogue integer NOT NULL,
    id_format smallint NOT NULL,
    date timestamp without time zone,
    length smallint,
    size real,
    sample_rate integer,
    chunk smallint,
    channels smallint,
    PRIMARY KEY (id_record)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.record_obs
(
    id_record_obs serial NOT NULL,
    id_record integer NOT NULL,
    observation character varying(100),
    PRIMARY KEY (id_record_obs)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.record_path
(
    id_record_path serial NOT NULL,
    id_record integer NOT NULL,
    record_path character varying(100),
    fingerprint character varying(100),
    PRIMARY KEY (id_record_path)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.sampling
(
    id_sampling serial NOT NULL,
    id_project smallint NOT NULL,
    id_cataloger smallint NOT NULL,
    id_season smallint NOT NULL,
    date timestamp without time zone,
    description character varying(100),
    PRIMARY KEY (id_sampling)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.season
(
    id_season smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_season)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.supply
(
    id_supply smallserial NOT NULL,
    description character varying NOT NULL,
    PRIMARY KEY (id_supply)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.type
(
    id_type smallint NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_type)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica."user"
(
    id_user smallserial NOT NULL,
    name character varying(100),
    password character varying(100),
    email character varying(100) NOT NULL,
    username character varying(100),
    last_login date,
    is_admin boolean,
    is_active boolean,
    is_staff boolean,
    is_superuser boolean,
    roles character varying(50) NOT NULL,
    PRIMARY KEY (id_user)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.country
(
    id_country smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_country)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.department
(
    id_department smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_department)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.vereda
(
    id_vereda smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_vereda)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.locality
(
    id_locality smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_locality)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.municipality
(
    id_municipality smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_municipality)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.voucher
(
    id_voucher serial NOT NULL,
    id_catalogue integer NOT NULL,
    voucher character varying(100),
    PRIMARY KEY (id_voucher)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.frequency_detail
(
    id_frequency_detail serial NOT NULL,
    id_labeled integer NOT NULL,
    begining integer,
    ending integer,
    minimal integer,
    maximun integer,
    peak integer,
    PRIMARY KEY (id_frequency_detail)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.time_detail
(
    id_time_detail serial NOT NULL,
    id_labeled integer NOT NULL,
    beging smallint,
    ending smallint,
    PRIMARY KEY (id_time_detail)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.software
(
    id_software smallserial NOT NULL,
    description character varying(80) NOT NULL,
    PRIMARY KEY (id_software)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.pulse_type
(
    id_pulse_type smallserial NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_pulse_type)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.measure
(
    id_measure smallserial NOT NULL,
    description character varying NOT NULL,
    PRIMARY KEY (id_measure)
)
WITH (
    OIDS = FALSE
);


CREATE TABLE bioacustica.microphone
(
    id_microphone smallint NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_microphone)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.gain
(
    id_gain smallint NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_gain)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.filter
(
    id_filter smallint NOT NULL,
    description character varying(100) NOT NULL,
    PRIMARY KEY (id_filter)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_case)
    REFERENCES bioacustica."case" (id_case)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_collector)
    REFERENCES bioacustica."user" (id_user)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_datum)
    REFERENCES bioacustica.datum (id_datum)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_h_serial)
    REFERENCES bioacustica.h_serial (id_h_serial)
    NOT VALID;

CREATE TABLE bioacustica.keys
(
    username character varying(200) NOT NULL,
    key character varying(200)  NOT NULL
)
WITH (
    OIDS = FALSE
);

ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_case)
    REFERENCES bioacustica."case" (id_case)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_collector)
    REFERENCES bioacustica."user" (id_user)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_datum)
    REFERENCES bioacustica.datum (id_datum)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_h_serial)
    REFERENCES bioacustica.h_serial (id_h_serial)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_habitat)
    REFERENCES bioacustica.habitat (id_habitat)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_memory)
    REFERENCES bioacustica.memory (id_memory)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_precision)
    REFERENCES bioacustica."precision" (id_precision)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_habitat)
    REFERENCES bioacustica.habitat (id_habitat)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_precision)
    REFERENCES bioacustica."precision" (id_precision)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_sampling)
    REFERENCES bioacustica.sampling (id_sampling)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_supply)
    REFERENCES bioacustica.supply (id_supply)
    NOT VALID;


ALTER TABLE bioacustica.catalogue_obs
    ADD FOREIGN KEY (id_catalogue)
    REFERENCES bioacustica.catalogue (id_catalogue)
    NOT VALID;


ALTER TABLE bioacustica.h_serial
    ADD FOREIGN KEY (id_hardware)
    REFERENCES bioacustica.hardware (id_hardware)
    NOT VALID;


ALTER TABLE bioacustica.label
    ADD FOREIGN KEY (id_type)
    REFERENCES bioacustica.type (id_type)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_evidence)
    REFERENCES bioacustica.evidence (id_evidence)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_label)
    REFERENCES bioacustica.label (id_label)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_labeler)
    REFERENCES bioacustica."user" (id_user)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_record)
    REFERENCES bioacustica.record (id_record)
    NOT VALID;


ALTER TABLE bioacustica.photo_path
    ADD FOREIGN KEY (id_catalogue)
    REFERENCES bioacustica.catalogue (id_catalogue)
    NOT VALID;


ALTER TABLE bioacustica.project
    ADD FOREIGN KEY (id_funding)
    REFERENCES bioacustica.funding (id_funding)
    NOT VALID;


ALTER TABLE bioacustica.record
    ADD FOREIGN KEY (id_catalogue)
    REFERENCES bioacustica.catalogue (id_catalogue)
    NOT VALID;


ALTER TABLE bioacustica.record
    ADD FOREIGN KEY (id_format)
    REFERENCES bioacustica.format (id_format)
    NOT VALID;


ALTER TABLE bioacustica.record_obs
    ADD FOREIGN KEY (id_record)
    REFERENCES bioacustica.record (id_record)
    NOT VALID;


ALTER TABLE bioacustica.record_path
    ADD FOREIGN KEY (id_record)
    REFERENCES bioacustica.record (id_record)
    NOT VALID;


ALTER TABLE bioacustica.sampling
    ADD FOREIGN KEY (id_cataloger)
    REFERENCES bioacustica."user" (id_user)
    NOT VALID;


ALTER TABLE bioacustica.sampling
    ADD FOREIGN KEY (id_project)
    REFERENCES bioacustica.project (id_project)
    NOT VALID;


ALTER TABLE bioacustica.sampling
    ADD FOREIGN KEY (id_season)
    REFERENCES bioacustica.season (id_season)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_department)
    REFERENCES bioacustica.department (id_department)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_country)
    REFERENCES bioacustica.country (id_country)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_municipality)
    REFERENCES bioacustica.municipality (id_municipality)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_vereda)
    REFERENCES bioacustica.vereda (id_vereda)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_locality)
    REFERENCES bioacustica.locality (id_locality)
    NOT VALID;


ALTER TABLE bioacustica.voucher
    ADD FOREIGN KEY (id_voucher)
    REFERENCES bioacustica.catalogue (id_catalogue)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_pulse_type)
    REFERENCES bioacustica.pulse_type (id_pulse_type)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_software)
    REFERENCES bioacustica.software (id_software)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_measure)
    REFERENCES bioacustica.measure (id_measure)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_frequency_detail)
    REFERENCES bioacustica.frequency_detail (id_frequency_detail)
    NOT VALID;


ALTER TABLE bioacustica.labeled
    ADD FOREIGN KEY (id_time_detail)
    REFERENCES bioacustica.time_detail (id_time_detail)
    NOT VALID;

ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_gain)
    REFERENCES bioacustica.gain (id_gain)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_filter)
    REFERENCES bioacustica.filter (id_filter)
    NOT VALID;


ALTER TABLE bioacustica.catalogue
    ADD FOREIGN KEY (id_microphone)
    REFERENCES bioacustica.microphone (id_microphone)
    NOT VALID;

END;

/* Desde este punto comienzan las funciones que se crearon y se integraron con django */

--Esta es la función que crea el admin en la base de datos
create or replace function bioacustica.create_user_admin (
  unm varchar,
  pwd varchar
)
returns varchar(10) as $$
begin



  execute format($f$create role %I login password '%s'$f$,unm,pwd);
  execute format('alter role %I SUPERUSER CREATEDB CREATEROLE',unm);
  execute format('alter role %I SET search_path TO bioacustica',unm);
  execute format('GRANT USAGE ON SCHEMA bioacustica TO %I',unm);
  execute format('SET search_path TO bioacustica');
  execute format('GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA bioacustica TO %I ',unm);
  return 'success';



end;
$$ language plpgsql;


-- Esta es la función que crea el colaborador de registros

create or replace function bioacustica.create_user_registros (
  unm varchar,
  pwd varchar
)
  returns varchar(10) as $$



begin



  execute format($f$create role %I login password '%s'$f$,unm,pwd);
  execute format('alter role %I NOSUPERUSER NOCREATEDB NOCREATEROLE',unm);
  execute format('alter role %I SET search_path TO bioacustica',unm);
  execute format('REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA bioacustica FROM %I',unm);
  execute format('REVOKE USAGE ON SCHEMA bioacustica FROM %I',unm);
  execute format('GRANT USAGE ON SCHEMA bioacustica TO %I',unm);
  execute format('SET search_path TO bioacustica');
  execute format('GRANT SELECT, INSERT, UPDATE ON TABLE label, labeled TO %I ',unm);
  execute format('GRANT SELECT, INSERT, UPDATE ON TABLE record, record_obs, record_path, format, season, project, habitat, hardware, h_serial, memory, gain, filter, microphone, precision, sampling, supply, catalogue TO %I ',unm);
  return 'success'; 



end;
$$ language plpgsql;


-- Esta es la función de el colaborador  de etiquetado
create or replace function bioacustica.create_user_etiquetado (
  unm varchar,
  pwd varchar
)
  returns varchar(10) as $$



begin



  execute format($f$create role %I login password '%s'$f$,unm,pwd);
  execute format('alter role %I NOSUPERUSER NOCREATEDB NOCREATEROLE',unm);
  execute format('alter role %I SET search_path TO bioacustica',unm);
  execute format('REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA bioacustica FROM %I',unm);
  execute format('REVOKE USAGE ON SCHEMA bioacustica FROM %I',unm);
  execute format('GRANT USAGE ON SCHEMA bioacustica TO %I',unm);
  execute format('SET search_path TO bioacustica');
  execute format('GRANT SELECT, INSERT, UPDATE ON TABLE label, labeled TO %I ',unm);
  execute format('GRANT SELECT ON TABLE record, record_obs, record_path, format, season, project, habitat, catalogue TO %I ',unm);
  return 'success';



end;
$$ language plpgsql;


-- Esta es la función para los usuarios

create or replace function bioacustica.create_user_usuario (
  unm varchar,
  pwd varchar
)
  returns varchar(10) as $$



begin



  execute format($f$create role %I login password '%s'$f$,unm,pwd);
  execute format('alter role %I NOSUPERUSER NOCREATEDB NOCREATEROLE',unm);
  execute format('alter role %I SET search_path TO bioacustica',unm);
  execute format('REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA bioacustica FROM %I',unm);
  execute format('REVOKE USAGE ON SCHEMA bioacustica FROM %I',unm);
  execute format('GRANT USAGE ON SCHEMA bioacustica TO %I',unm);
  execute format('SET search_path TO bioacustica');
  execute format('GRANT SELECT ON TABLE label, labeled TO %I ',unm);
  execute format('GRANT SELECT ON TABLE record, record_obs, record_path, format, season, project, habitat TO %I ',unm);
  return 'success';



end;
$$ language plpgsql;

-- Esta función tiene como utilidad cambiar la contraseña dentro de la DB, no afecta la tabla users.

create or replace function bioacustica.change_password (
  unm varchar,
  pwd varchar
)
  returns varchar(10) as $$



begin
  execute format($f$alter role %I with password '%s'$f$,unm,pwd);
  return 'success';



end;
$$ language plpgsql;


create or replace function bioacustica.drop_user (
  unm varchar
)
  returns varchar(10) as $$



begin
  execute format('REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA bioacustica FROM %I',unm);
  execute format('REVOKE USAGE ON SCHEMA bioacustica FROM %I',unm);
  execute format('DROP USER %I ',unm);
  return 'success';



end;
$$ language plpgsql;

--tabla de filtros si no se espeficica un parametro se toma como Null--

create or replace function bioacustica.get_join(
    catalogo varchar default NULL,
    habitat_q varchar default NULL,
    municipio varchar default NULL,
    evento_q varchar default NULL,
    tipo_case varchar default NULL,
    tipo_micro varchar default NULL,
    metodo_etiquetado varchar default NULL,
    software_q varchar default NULL,
    tipo_grabadora varchar default NULL
)

    returns table (
        id_record integer,
        formato_ varchar,
        chunk_ smallint,
        date_record_ timestamp,
        fingerprint_ varchar,
        catalogo_ varchar,
        elevation integer,
        chunks_ smallint,
        tipo_grabadora_ varchar,
        case_ varchar,
        microphone varchar,
        sampling_description varchar,
        habitat_ varchar,
        ciudad_ varchar,
        departamento_ varchar,
        type_ varchar,
        metodo_etiquetado_ varchar,
        software_etiquetado_ varchar
    )

    language plpgsql
as $$
begin
    return query
        select
            record.id_record,
            format.description,
            record.chunk,
            record.date as date_record,
            record_path.fingerprint,
            catalogue.description,
            catalogue.elevation,
            catalogue.chunks,
            hardware.description,
            "case".description,
            microphone.description,
            sampling.description,
            habitat.description,
            municipality.description,
            department.description,
            type.description,
            evidence.description,
            software.description

        from
            catalogue
        INNER JOIN record ON catalogue.id_catalogue=record.id_catalogue
        INNER JOIN record_path ON record.id_record=record_path.id_record
        --where catalogue.description = (CASE WHEN catalogo IS NOT NULL THEN catalogo ELSE catalogue.description END)
        INNER JOIN format ON record.id_format=format.id_format
        INNER JOIN h_serial ON catalogue.id_h_serial=h_serial.id_h_serial
        INNER JOIN hardware ON h_serial.id_hardware=hardware.id_hardware
        INNER JOIN "case" ON catalogue.id_case="case".id_case
        INNER JOIN microphone ON catalogue.id_microphone=microphone.id_microphone
        INNER JOIN sampling ON catalogue.id_sampling=sampling.id_sampling
        INNER JOIN habitat ON catalogue.id_habitat=habitat.id_habitat
        INNER JOIN municipality ON catalogue.id_municipality=municipality.id_municipality
        INNER JOIN department ON catalogue.id_department=department.id_department
        LEFT OUTER JOIN labeled ON record.id_record=labeled.id_record
        LEFT OUTER JOIN label ON labeled.id_label=label.id_label
        LEFT OUTER JOIN type ON label.id_type=type.id_type
        LEFT OUTER JOIN evidence ON labeled.id_evidence=evidence.id_evidence
        LEFT OUTER JOIN software ON labeled.id_software=software.id_software

        where municipality.description = (CASE WHEN municipio IS NOT NULL THEN municipio ELSE municipality.description END)
        and   catalogue.description = (CASE WHEN catalogo IS NOT NULL THEN catalogo ELSE catalogue.description END)
        and   habitat.description = (CASE WHEN habitat_q IS NOT NULL THEN habitat_q ELSE habitat.description END)
        --and   type.description = (CASE WHEN evento_q IS NOT NULL THEN evento_q ELSE type.description END)
        and   "case".description = (CASE WHEN tipo_case IS NOT NULL THEN tipo_case ELSE "case".description END)
        and   microphone.description = (CASE WHEN tipo_micro IS NOT NULL THEN tipo_micro ELSE microphone.description END)
        --and   evidence.description = (CASE WHEN metodo_etiquetado IS NOT NULL THEN metodo_etiquetado ELSE evidence.description END)
        --and   software.description = (CASE WHEN software_q IS NOT NULL THEN software_q ELSE software.description END)
        --and   hardware.description = (CASE WHEN tipo_grabadora IS NOT NULL THEN tipo_grabadora ELSE hardware.description END)
        ;
end;$$

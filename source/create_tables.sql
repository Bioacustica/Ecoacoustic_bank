--java -jar schemaspy-6.1.0.jar -configFile schema_spy.properties

BEGIN;

CREATE SCHEMA bioacustica;

CREATE TABLE bioacustica."case"
(
    id_case smallserial NOT NULL,
    description character varying(100),
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
    id_gain integer NOT NULL,
    id_filters integer NOT NULL,
    id_collector smallint NOT NULL,
    id_h_serial smallint NOT NULL,
    id_supply smallint NOT NULL,
    id_case smallint NOT NULL,
    id_memory smallint NOT NULL,
    id_habitat smallint NOT NULL,
    id_precision smallint NOT NULL,
    id_datum smallint NOT NULL,
    elevation integer,
    coordinates point,
    height integer,
    chunks smallint,
    size real,
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
    description character varying(100),
    PRIMARY KEY (id_datum)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.evidence
(
    id_evidence smallserial NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_evidence)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.format
(
    id_format smallserial NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_format)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.funding
(
    id_funding smallserial NOT NULL,
    description character varying(100),
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
    description character varying(100),
    PRIMARY KEY (id_habitat)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.hardware
(
    id_hardware smallserial NOT NULL,
    description character varying,
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
    description character varying(100),
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
    description character varying(100),
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
    description character varying(100),
    PRIMARY KEY (id_season)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.supply
(
    id_supply smallserial NOT NULL,
    description character varying,
    PRIMARY KEY (id_supply)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.type
(
    id_type smallint NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_type)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE IF NOT EXISTS bioacustica.USER
(
    ID_USER SERIAL,
    USERNAME character varying(100),
    PASSWORD character varying(100),
    EMAIL character varying(100),
    LAST_LOGIN DATE,
    IS_ADMIN BOOLEAN,
    IS_ACTIVE BOOLEAN,
    IS_STAFF BOOLEAN,
    IS_SUPERUSER BOOLEAN,
    ROLES character varying(50),
    PRIMARY KEY (ID_USER)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.country
(
    id_country smallserial NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_country)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.department
(
    id_department smallserial NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_department)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.vereda
(
    id_vereda smallserial NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_vereda)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.locality
(
    id_locality smallserial NOT NULL,
    description character varying(100),
    PRIMARY KEY (id_locality)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE bioacustica.municipality
(
    id_municipality smallserial NOT NULL,
    description character varying(100),
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
    descripton character varying(80) NOT NULL,
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

END;
BEGIN;


CREATE TABLE public.FUNDING
(
    ID_FUNDING SERIAL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_FUNDING)
);

CREATE TABLE public.PROJECT
(
    ID_PROJECT integer NOT NULL,
    ID_FUNDING integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_PROJECT)
);

CREATE TABLE public.SEASON
(
    ID_SEASON integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_SEASON)
);

CREATE TABLE public.STUDIO
(
    ID_STUDIO integer NOT NULL,
    ID_PROJECT integer NOT NULL,
    ID_CATALOGER integer NOT NULL,
    ID_SEASON integer NOT NULL,
    DATE timestamp without time zone,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_STUDIO)
);

CREATE TABLE public.USER
(
    ID_USER integer NOT NULL,
    NAME character varying(100),
    EMAIL character varying(100),
    PRIMARY KEY (ID_USER)
);

CREATE TABLE public.TYPE
(
    ID_TYPE integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_TYPE)
);

CREATE TABLE public.EVENT
(
    ID_EVENT integer NOT NULL,
    ID_TYPE integer NOT NULL,
    PRIMARY KEY (ID_EVENT)
);

CREATE TABLE public.EVIDENCE
(
    ID_EVIDENCE integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_EVIDENCE)
);

CREATE TABLE public.PRECISION
(
    ID_PRECISION integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_PRECISION)
);

CREATE TABLE public.DATUM
(
    ID_DATUM integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_DATUM)
);

CREATE TABLE public.FORMAT
(
    ID_FORMAT integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_FORMAT)
);

CREATE TABLE public.RECORD_OBS
(
    ID_RECORD_OBS integer NOT NULL,
    ID_RECORD integer NOT NULL,
    OBSERVATION character varying(100),
    PRIMARY KEY (ID_RECORD_OBS)
);

CREATE TABLE public.CATALOG_OBS
(
    ID_CATALOG_OBS integer NOT NULL,
    ID_CATALOG integer NOT NULL,
    OBSERVATION character varying(100),
    PRIMARY KEY (ID_CATALOG_OBS)
);

CREATE TABLE public.HABITAT
(
    ID_HABITAT integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_HABITAT)
);

CREATE TABLE public.MEMORY
(
    ID_MEMORY integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_MEMORY)
);

CREATE TABLE public.CASE
(
    ID_CASE integer NOT NULL,
    DESCRIPTION character varying(100),
    PRIMARY KEY (ID_CASE)
);

CREATE TABLE public.SUPPLY
(
    ID_SUPPLY integer NOT NULL,
    DESCRIPTION character varying,
    PRIMARY KEY (ID_SUPPLY)
);

CREATE TABLE public.HARDWARE
(
    ID_HARDWARE integer NOT NULL,
    DESCRIPTION character varying,
    PRIMARY KEY (ID_HARDWARE)
);

CREATE TABLE public.LABELED
(
    ID_LABELED integer NOT NULL,
    ID_EVENT integer NOT NULL,
    ID_RECORD integer NOT NULL,
    ID_EVIDENCE integer NOT NULL,
    ID_LABELER integer NOT NULL,
    BEGIN integer,
    LABEL_END integer,
    PRIMARY KEY (ID_LABELED)
);

CREATE TABLE public.RECORD
(
    ID_RECORD integer NOT NULL,
    ID_CATALOG integer NOT NULL,
    ID_FORMAT integer NOT NULL,
    FINGERPRINT character varying(64),
    PATH character varying(150),
    DATE timestamp without time zone,
    LENGTH integer,
    SIZE real,
    SAMPLE_RATE integer,
    CHUNK integer,
    CHANNELS integer,
    PRIMARY KEY (ID_RECORD)
);

CREATE TABLE public.CATALOG
(
    ID_CATALOG integer NOT NULL,
    ID_STUDIO integer NOT NULL,
    ID_COLLECTOR integer NOT NULL,
    ID_SERIAL integer NOT NULL,
    ID_SUPPLY integer NOT NULL,
    ID_CASE integer NOT NULL,
    ID_MEMORY integer NOT NULL,
    ID_HABITAT integer NOT NULL,
    ID_PRECISION integer NOT NULL,
    ID_DATUM integer NOT NULL,
    ELEVATION integer,
    COORDINATES point,
    HEIGHT integer,
    CHUNKS integer,
    SIZE real,
    PRIMARY KEY (ID_CATALOG)
);

ALTER TABLE public.PROJECT
    ADD FOREIGN KEY (ID_FUNDING)
    REFERENCES public.FUNDING (ID_FUNDING)
    NOT VALID;


ALTER TABLE public.STUDIO
    ADD FOREIGN KEY (ID_CATALOGER)
    REFERENCES public.USER (ID_USER)
    NOT VALID;


ALTER TABLE public.STUDIO
    ADD FOREIGN KEY (ID_PROJECT)
    REFERENCES public.PROJECT (ID_PROJECT)
    NOT VALID;


ALTER TABLE public.STUDIO
    ADD FOREIGN KEY (ID_SEASON)
    REFERENCES public.SEASON (ID_SEASON)
    NOT VALID;


ALTER TABLE public.EVENT
    ADD FOREIGN KEY (ID_TYPE)
    REFERENCES public.TYPE (ID_TYPE)
    NOT VALID;


ALTER TABLE public.LABELED
    ADD FOREIGN KEY (ID_EVENT)
    REFERENCES public.EVENT (ID_EVENT)
    NOT VALID;


ALTER TABLE public.LABELED
    ADD FOREIGN KEY (ID_RECORD)
    REFERENCES public.RECORD (ID_RECORD)
    NOT VALID;


ALTER TABLE public.LABELED
    ADD FOREIGN KEY (ID_EVIDENCE)
    REFERENCES public.EVIDENCE (ID_EVIDENCE)
    NOT VALID;


ALTER TABLE public.LABELED
    ADD FOREIGN KEY (ID_EVIDENCE)
    REFERENCES public.EVIDENCE (ID_EVIDENCE)
    NOT VALID;


ALTER TABLE public.LABELED
    ADD FOREIGN KEY (ID_LABELER)
    REFERENCES public.USER (ID_USER)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_STUDIO)
    REFERENCES public.STUDIO (ID_STUDIO)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_COLLECTOR)
    REFERENCES public.USER (ID_USER)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_SUPPLY)
    REFERENCES public.SUPPLY (ID_SUPPLY)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_CASE)
    REFERENCES public.CASE (ID_CASE)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_MEMORY)
    REFERENCES public.MEMORY (ID_MEMORY)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_HABITAT)
    REFERENCES public.HABITAT (ID_HABITAT)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_PRECISION)
    REFERENCES public.PRECISION (ID_PRECISION)
    NOT VALID;


ALTER TABLE public.CATALOG
    ADD FOREIGN KEY (ID_DATUM)
    REFERENCES public.DATUM (ID_DATUM)
    NOT VALID;


ALTER TABLE public.RECORD
    ADD FOREIGN KEY (ID_FORMAT)
    REFERENCES public.FORMAT (ID_FORMAT)
    NOT VALID;


ALTER TABLE public.RECORD_OBS
    ADD FOREIGN KEY (ID_RECORD)
    REFERENCES public.RECORD (ID_RECORD)
    NOT VALID;


ALTER TABLE public.CATALOG_OBS
    ADD FOREIGN KEY (ID_CATALOG)
    REFERENCES public.CATALOG (ID_CATALOG)
    NOT VALID;

END;
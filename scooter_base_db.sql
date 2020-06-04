--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Debian 10.12-2.pgdg90+1)
-- Dumped by pg_dump version 12.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

--
-- Name: blobs; Type: TABLE; Schema: public; Owner: guillotina
--

CREATE TABLE public.blobs (
    bid character varying(64) NOT NULL,
    zoid character varying(64) NOT NULL,
    chunk_index integer NOT NULL,
    data bytea
);


ALTER TABLE public.blobs OWNER TO guillotina;

--
-- Name: objects; Type: TABLE; Schema: public; Owner: guillotina
--

CREATE TABLE public.objects (
    zoid character varying(64) NOT NULL,
    tid bigint NOT NULL,
    state_size bigint NOT NULL,
    part bigint NOT NULL,
    resource boolean NOT NULL,
    of character varying(64),
    otid bigint,
    parent_id character varying(64),
    id text,
    type text NOT NULL,
    json jsonb,
    state bytea
);


ALTER TABLE public.objects OWNER TO guillotina;

--
-- Name: tid_sequence; Type: SEQUENCE; Schema: public; Owner: guillotina
--

CREATE SEQUENCE public.tid_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tid_sequence OWNER TO guillotina;

--
-- Data for Name: blobs; Type: TABLE DATA; Schema: public; Owner: guillotina
--

COPY public.blobs (bid, zoid, chunk_index, data) FROM stdin;
\.


--
-- Data for Name: objects; Type: TABLE DATA; Schema: public; Owner: guillotina
--

COPY public.objects (zoid, tid, state_size, part, resource, of, otid, parent_id, id, type, json, state) FROM stdin;
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD	0	0	0	f	\N	\N	\N	\N	TRASH_REF	\N	\N
00000000000000000000000000000000	1	64	0	f	\N	0	\N	\N	guillotina.db.db.Root	null	\\x80049535000000000000008c106775696c6c6f74696e612e64622e6462948c04526f6f749493942981947d948c095f5f64625f69645f5f948c0264629473622e
8e0493de26a14da7987bec7697a86dce	2	441	0	t	\N	\N	00000000000000000000000000000000	scooter	Container	{"id": "scooter", "tid": null, "path": "/", "uuid": "8e0493de26a14da7987bec7697a86dce", "depth": 1, "title": "scooter", "type_name": "Container", "parent_uuid": "00000000000000000000000000000000", "access_roles": ["guillotina.Reader", "guillotina.Reviewer", "guillotina.Owner", "guillotina.Editor", "guillotina.ContainerAdmin"], "access_users": ["root"], "container_id": "scooter", "creation_date": "2020-06-01T22:09:25.978916+00:00", "modification_date": "2020-06-01T22:09:25.978916+00:00"}	\\x800495ae010000000000008c126775696c6c6f74696e612e636f6e74656e74948c09436f6e7461696e65729493942981947d94288c09747970655f6e616d659468018c0d6372656174696f6e5f64617465948c086461746574696d65948c086461746574696d65949394430a07e406011609190eefe4948c0e646174657574696c2e747a2e747a948c05747a757463949394298194869452948c116d6f64696669636174696f6e5f646174659468108c057469746c65948c0773636f6f746572948c0b6465736372697074696f6e948c00948c075f5f61636c5f5f947d948c087072696e726f6c65948c1f6775696c6c6f74696e612e73656375726974792e73656375726974796d6170948c0b53656375726974794d61709493942981947d94288c065f6279726f77947d94288c196775696c6c6f74696e612e436f6e7461696e657241646d696e947d948c04726f6f74948c1e6775696c6c6f74696e612e696e74657266616365732e7365637572697479948c05416c6c6f77949394738c106775696c6c6f74696e612e4f776e6572947d946822682573758c065f6279636f6c947d9468227d94286820682568266825757375627375622e
8e0|4761bc1468e0495ead4d1bb59939e8ae	3	502	0	t	\N	\N	8e0493de26a14da7987bec7697a86dce	patients	PatientFolder	{"id": "patients", "tid": null, "path": "/patients", "uuid": "8e0|4761bc1468e0495ead4d1bb59939e8ae", "depth": 2, "title": "Patients", "type_name": "PatientFolder", "parent_uuid": "8e0493de26a14da7987bec7697a86dce", "access_roles": ["guillotina.Reader", "guillotina.Reviewer", "guillotina.Owner", "guillotina.Editor", "guillotina.ContainerAdmin", "guillotina.Member"], "access_users": ["root"], "container_id": "scooter", "creation_date": "2020-06-01T22:10:20.062624+00:00", "modification_date": "2020-06-01T22:10:20.062624+00:00"}	\\x800495eb010000000000008c256775696c6c6f74696e615f73636f6f7465726d70692e636f6e74656e742e70617469656e74948c0d50617469656e74466f6c6465729493942981947d94288c09747970655f6e616d659468018c0d6372656174696f6e5f64617465948c086461746574696d65948c086461746574696d65949394430a07e40601160a1400f4a0948c0e646174657574696c2e747a2e747a948c05747a757463949394298194869452948c116d6f64696669636174696f6e5f646174659468108c0863726561746f7273948c04726f6f749485948c057469746c65948c0850617469656e7473948c0c636f6e7472696275746f72739468148c075f5f61636c5f5f947d948c08726f6c657065726d948c1f6775696c6c6f74696e612e73656375726974792e73656375726974796d6170948c0b53656375726974794d61709493942981947d94288c065f6279726f77947d94288c156775696c6c6f74696e612e416464436f6e74656e74947d948c116775696c6c6f74696e612e4d656d626572948c1e6775696c6c6f74696e612e696e74657266616365732e7365637572697479948c05416c6c6f77949394738c186775696c6c6f74696e612e416363657373436f6e74656e74947d946824682773758c065f6279636f6c947d9468247d94286822682768286827757375627375622e
8e0|6f87cb85bd204ce9b0963e0132d00f96	3	240	0	f	8e0493de26a14da7987bec7697a86dce	2	\N	_registry	guillotina.registry.Registry	null	\\x800495e5000000000000008c136775696c6c6f74696e612e7265676973747279948c0852656769737472799493942981947d94288c0464617461947d94288c346775696c6c6f74696e612e696e74657266616365732e72656769737472792e494c61796572732e6163746976655f6c6179657273942891948c2e6775696c6c6f74696e612e696e74657266616365732e72656769737472792e494164646f6e732e656e61626c656494288c156775696c6c6f74696e615f73636f6f7465726d7069949194758c026964948c095f7265676973747279948c085f5f6e616d655f5f948c095f72656769737472799475622e
\.


--
-- Name: tid_sequence; Type: SEQUENCE SET; Schema: public; Owner: guillotina
--

SELECT pg_catalog.setval('public.tid_sequence', 4, true);


--
-- Name: objects object_parent_id_zoid_check; Type: CHECK CONSTRAINT; Schema: public; Owner: guillotina
--

ALTER TABLE public.objects
    ADD CONSTRAINT object_parent_id_zoid_check CHECK (((parent_id)::text <> (zoid)::text)) NOT VALID;


--
-- Name: objects objects_pkey; Type: CONSTRAINT; Schema: public; Owner: guillotina
--

ALTER TABLE ONLY public.objects
    ADD CONSTRAINT objects_pkey PRIMARY KEY (zoid);


--
-- Name: blobs pk_blobs; Type: CONSTRAINT; Schema: public; Owner: guillotina
--

ALTER TABLE ONLY public.blobs
    ADD CONSTRAINT pk_blobs PRIMARY KEY (bid, zoid, chunk_index);


--
-- Name: blob_bid; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX blob_bid ON public.blobs USING btree (bid);


--
-- Name: blob_chunk; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX blob_chunk ON public.blobs USING btree (chunk_index);


--
-- Name: blob_zoid; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX blob_zoid ON public.blobs USING btree (zoid);


--
-- Name: object_id; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX object_id ON public.objects USING btree (id);


--
-- Name: object_of; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX object_of ON public.objects USING btree (of);


--
-- Name: object_parent; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX object_parent ON public.objects USING btree (parent_id);


--
-- Name: object_part; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX object_part ON public.objects USING btree (part);


--
-- Name: object_tid; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX object_tid ON public.objects USING btree (tid);


--
-- Name: object_type; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE INDEX object_type ON public.objects USING btree (type);


--
-- Name: objects_annotations_unique; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE UNIQUE INDEX objects_annotations_unique ON public.objects USING btree (of, id);


--
-- Name: objects_parent_id_id_key; Type: INDEX; Schema: public; Owner: guillotina
--

CREATE UNIQUE INDEX objects_parent_id_id_key ON public.objects USING btree (parent_id, id) WHERE ((parent_id)::text <> 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'::text);


--
-- Name: blobs blobs_zoid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: guillotina
--

ALTER TABLE ONLY public.blobs
    ADD CONSTRAINT blobs_zoid_fkey FOREIGN KEY (zoid) REFERENCES public.objects(zoid) ON DELETE CASCADE;


--
-- Name: objects objects_of_fkey; Type: FK CONSTRAINT; Schema: public; Owner: guillotina
--

ALTER TABLE ONLY public.objects
    ADD CONSTRAINT objects_of_fkey FOREIGN KEY (of) REFERENCES public.objects(zoid) ON DELETE CASCADE;


--
-- Name: objects objects_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: guillotina
--

ALTER TABLE ONLY public.objects
    ADD CONSTRAINT objects_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES public.objects(zoid) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--


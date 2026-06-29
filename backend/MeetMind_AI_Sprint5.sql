--
-- PostgreSQL database dump
--

\restrict XuY0EISxCcK9Jh3nead8cbakEOq6x3wgR8MgpxLCSJyMKsbpqjOMI2lMyVEci5N

-- Dumped from database version 17.10
-- Dumped by pg_dump version 17.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: meetingstatus; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.meetingstatus AS ENUM (
    'UPLOADED',
    'PROCESSING',
    'TRANSCRIBED',
    'SUMMARIZED',
    'COMPLETED',
    'FAILED'
);


ALTER TYPE public.meetingstatus OWNER TO postgres;

--
-- Name: meetingtype; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.meetingtype AS ENUM (
    'BUSINESS',
    'LECTURE',
    'WEBINAR',
    'WORKSHOP',
    'INTERVIEW',
    'PERSONAL'
);


ALTER TYPE public.meetingtype OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: meeting_analysis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.meeting_analysis (
    id integer NOT NULL,
    meeting_id integer NOT NULL,
    summary text NOT NULL,
    minutes_of_meeting text NOT NULL,
    action_items jsonb NOT NULL,
    decisions jsonb NOT NULL,
    key_topics jsonb NOT NULL,
    sentiment character varying(30) NOT NULL,
    model_name character varying(100) NOT NULL,
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE public.meeting_analysis OWNER TO postgres;

--
-- Name: meeting_analysis_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.meeting_analysis_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.meeting_analysis_id_seq OWNER TO postgres;

--
-- Name: meeting_analysis_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.meeting_analysis_id_seq OWNED BY public.meeting_analysis.id;


--
-- Name: meetings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.meetings (
    id integer NOT NULL,
    user_id integer NOT NULL,
    title character varying(255) NOT NULL,
    description text,
    meeting_type public.meetingtype NOT NULL,
    recording_path character varying(1000) NOT NULL,
    original_filename character varying(255) NOT NULL,
    duration_seconds integer,
    processing_status public.meetingstatus NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.meetings OWNER TO postgres;

--
-- Name: meetings_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.meetings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.meetings_id_seq OWNER TO postgres;

--
-- Name: meetings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.meetings_id_seq OWNED BY public.meetings.id;


--
-- Name: transcripts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transcripts (
    id integer NOT NULL,
    meeting_id integer NOT NULL,
    transcript_text text NOT NULL,
    language character varying(20) NOT NULL,
    model_name character varying(50) NOT NULL,
    processing_time double precision,
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE public.transcripts OWNER TO postgres;

--
-- Name: transcripts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transcripts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.transcripts_id_seq OWNER TO postgres;

--
-- Name: transcripts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transcripts_id_seq OWNED BY public.transcripts.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    full_name character varying(100) NOT NULL,
    email character varying(255) NOT NULL,
    hashed_password character varying(255) NOT NULL,
    is_active boolean,
    is_verified boolean,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: meeting_analysis id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meeting_analysis ALTER COLUMN id SET DEFAULT nextval('public.meeting_analysis_id_seq'::regclass);


--
-- Name: meetings id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meetings ALTER COLUMN id SET DEFAULT nextval('public.meetings_id_seq'::regclass);


--
-- Name: transcripts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transcripts ALTER COLUMN id SET DEFAULT nextval('public.transcripts_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
95f715ecbb5a
\.


--
-- Data for Name: meeting_analysis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.meeting_analysis (id, meeting_id, summary, minutes_of_meeting, action_items, decisions, key_topics, sentiment, model_name, created_at) FROM stdin;
\.


--
-- Data for Name: meetings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.meetings (id, user_id, title, description, meeting_type, recording_path, original_filename, duration_seconds, processing_status, created_at, updated_at) FROM stdin;
1	1	RL Seminar	Reinforcement Learning Discussion	PERSONAL	uploads\\meetings\\1337c352-b97a-4c1c-8033-3e529ac9a419.mp4	Alice_in_Borderland_S01E01_480p_WEB_DL_HIN_ENG_x264_MSubs_KatmovieHD.mp4	\N	UPLOADED	2026-06-27 17:41:45.471771	2026-06-27 17:41:45.471771
2	1	video	testing	PERSONAL	uploads\\meetings\\c1205e52-38d6-43ea-9142-be71a7725980.mp4	Alice_in_Borderland_S01E01_480p_WEB_DL_HIN_ENG_x264_MSubs_KatmovieHD.mp4	\N	COMPLETED	2026-06-29 10:24:03.665955	2026-06-29 10:52:29.078935
3	1	vid	test	PERSONAL	uploads\\meetings\\1aaa9f12-bc05-40ea-8887-2eb8944f26c1.mp4	YTMP3GG_YouTube_here-s-a-10-second-joke-because-you-re-b_Media_FAyKDaXEAgc_003_480p.mp4	\N	COMPLETED	2026-06-29 11:14:38.830926	2026-06-29 11:14:59.425647
4	1	Test Meeting	Testing Whisper	PERSONAL	uploads\\meetings\\de602755-b3ca-4c7c-81b6-cdb18929699f.mp4	YTMP3GG_YouTube_here-s-a-10-second-joke-because-you-re-b_Media_FAyKDaXEAgc_003_480p.mp4	\N	COMPLETED	2026-06-29 11:17:07.348219	2026-06-29 11:17:19.144246
\.


--
-- Data for Name: transcripts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transcripts (id, meeting_id, transcript_text, language, model_name, processing_time, created_at) FROM stdin;
1	2	― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― � چیتا رہنا, تمہیں تو مفت کی کھنے میں مزادہ ہے چلتا ہوں, تمہاری باکوہ سون کے پاکیا کاش سندگی بھی ریسٹ ہو سکتے جب مومتی تو سب کیتنا چا تھا یہ تم اپنے بھائی حاجمی کے راستے میں مطاو چلتا ہوں, تمہاری باکوہ چلتا ہوں ماری باکو ہوں تمہاری باکوہ چلتا ہوں چلتا ہوں ... ... ... ... ... ... ... ... ... ... ... ... ... ... Mast Calum, ... ..all over them all over the world. I won't be able to pay more. Why do they keep wanting to lay down on the back? We are screwed. This is less. D씩an, Departure.. .. wastes the steadily gaining energy with the sue department. However... Shukriyo? ... a a a nd nd ‰ In their love, they're wounded doves I am ‰ I eat people, we don't think they're making money ‰ We eat men, neat a meeting ‰ could you say something to them? ‰ Che Bet cost a meal heart fatigue Aciste, kailasisur True. Mook vaa yeer Marx. ators. Ga familiarize her. Nurtualiz puritatakri intimidating. Amnibсuru n onean diei. ... plasticine with bird, and intelligence needs its Hilfe. Hela, insatiate ls caramel, and it is Merit! Use yeaun ans Fane! Lekker schwaan anasein ni belidana i тип ala bhaaatcharga? ... ohab Ladies and Gentlemen, ala bhaa금al hela scrab ? Haa? Hotsky, what is it? ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― � ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ ‒ � ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...iqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaqaq ṭhIGG Wwall ? 30 ecologicalants ? ..dha Bachelorziard, can expand or else l may be killed ... ..to the end of my life. lt is not that. ..it depends on you. Daanudu you can devour it. ..just be dresseschiard. Who are you ? ...todor algo? 10 secondes. ...todor, 4. 2nd half. ...todor. ....todor... ...todor... ...todor... ‏Wouh! ‏Wouh! ‏Changement. ...taggai tainme kisi eko saatrufais karna hooga. ...segrifais? Indarwazu ke nam sahi nahi hei. Sawal i hei ki ini kholega korn. ...kuki jo bhi kholega, wo khatre me hooga. ...kusna kiki jaan ubhari vijasakai. ...kogla darwaza tum kiur eek hulti. ...muje lakta hai mera jina, insano ko bhajaanke lii sahi hooga. Ei kya bakwaz karna hei tu? ...1 minut. ...hasse to kui bi darwaza nahi kholega. ...kortan khatme hooga da saab eek saatrufais saatrufais karna hooga. ...tum kiur eek hulti. ...tum ea saan lakta hai to hulti kholega. ...dus saakamatke haitri raho. ...tupir mei khola hooga. ...hari sui. ...haitri kiur eek hulti hulti khaatri raho. ...haitri kiur eek hulti khaatri raho. ...geniz langenur. Aaris. Deoga? Tummi, nek'i khol pa'lla bhaar a'i hoo hiannig? Aise me, tummi na'i hoo slo ka'i hoo lakher. Deoga! 20 second-vace hai. Maakodi khol ki haka kayaa? Aise bi hai pannaati hai. Karpe hai? Aa bhaar i baary hai. ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― � ... года , ... ‒ Code. ‒ Code. ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― � ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― � D'haiaat nao, weak toa, weak toa. Bixi on da, you must be surprised, Nooo. Aarishu! Bixi on da, weak. Bixi on da, weak. Bixi! ... ... ... ... Ай! Ай! Sa además, Pwetherh d' domain. Chuaanay! Bada a'a esad nashirem gaa you gy atti ki onions.. Since you are here. And with no reason. If it's proof before the door is activated why did it open. Stop. ford i missed something. 52 cm kids who were left corner. We are in the room right now under the last corner. اquentی و لكن نہیں اتنی ایک Oprah ‒ ‒ ‒ ‒ ‒ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .	nn	base	965.28	2026-06-29 10:52:28.956329
2	3	Hey buddy how was school? Everybody was mocking me. Why everybody was mocking you? It was mocking you! It was Mario, it was mocking you! Why everybody's mocking you!	en	base	13.23	2026-06-29 11:14:59.398211
3	4	Hey buddy how was school? Everybody was mocking me. Why everybody was mocking you? It was mocking you all! It was Mario! Mark it out! Why everybody's mocking you all!	en	base	6.98	2026-06-29 11:17:19.131337
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, full_name, email, hashed_password, is_active, is_verified, created_at, updated_at) FROM stdin;
1	rohini koli	rohini@example.com	$2b$12$8Andxs/gXJU0En2iF9BK/eyziXg8P1CZ2IkIm7SNoCWBZjn7D7N3S	t	f	2026-06-26 17:15:55.974891	2026-06-26 17:15:55.974891
2	Rohini Koli	rohini10@example.com	$2b$12$fYImu8noJxACpfQ9ERCUsu8IhV6SO3tb5t95My3Oc7ICquxPpBrmG	t	f	2026-06-27 16:52:55.861725	2026-06-27 16:52:55.861725
\.


--
-- Name: meeting_analysis_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.meeting_analysis_id_seq', 1, false);


--
-- Name: meetings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.meetings_id_seq', 4, true);


--
-- Name: transcripts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transcripts_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: meeting_analysis meeting_analysis_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meeting_analysis
    ADD CONSTRAINT meeting_analysis_pkey PRIMARY KEY (id);


--
-- Name: meetings meetings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meetings
    ADD CONSTRAINT meetings_pkey PRIMARY KEY (id);


--
-- Name: transcripts transcripts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transcripts
    ADD CONSTRAINT transcripts_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_meeting_analysis_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_meeting_analysis_id ON public.meeting_analysis USING btree (id);


--
-- Name: ix_meeting_analysis_meeting_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_meeting_analysis_meeting_id ON public.meeting_analysis USING btree (meeting_id);


--
-- Name: ix_meetings_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_meetings_id ON public.meetings USING btree (id);


--
-- Name: ix_meetings_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_meetings_user_id ON public.meetings USING btree (user_id);


--
-- Name: ix_transcripts_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_transcripts_id ON public.transcripts USING btree (id);


--
-- Name: ix_transcripts_meeting_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_transcripts_meeting_id ON public.transcripts USING btree (meeting_id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: meeting_analysis meeting_analysis_meeting_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meeting_analysis
    ADD CONSTRAINT meeting_analysis_meeting_id_fkey FOREIGN KEY (meeting_id) REFERENCES public.meetings(id) ON DELETE CASCADE;


--
-- Name: meetings meetings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meetings
    ADD CONSTRAINT meetings_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: transcripts transcripts_meeting_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transcripts
    ADD CONSTRAINT transcripts_meeting_id_fkey FOREIGN KEY (meeting_id) REFERENCES public.meetings(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict XuY0EISxCcK9Jh3nead8cbakEOq6x3wgR8MgpxLCSJyMKsbpqjOMI2lMyVEci5N


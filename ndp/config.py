# leave it to 0 to get data from all years, change it for example 2023, 2022 to get data of specific year
year = 0
mappings = [
    {
        'Koshi': {
            'Taplejung': {
                'Phaktanglung Rural Municipality': 1,
                'Maiwakhola Rural Municipality': 2,
                'Meringden Rural Municipality': 3,
                'Maiwakhola Rural Municipality': 4,
                'Aathrai Triveni Rural Municipality': 5,
                'Phungling Municipality': 6,
                'Pathibhara Yangwarak Rural Municipality': 7,
                'Sirijangha Rural Municipality': 8,
                'Sidingwa Rural Municipality': 9

            },
            'Sankhuwasabha': {
                'Bhotkhola Rural Municipality': 10,
                'Makalu Rural Municipality': 11,
                'Silichong Rural Municipality': 12,
                'Chichila Rural Municipality': 13,
                'Sabhapokhari Rural Municipality': 14,
                'Khandbari Municipality': 15,
                'Panchkhapan Municipality': 16,
                'Chainpur Municipality': 17,
                'Madi Municipality': 18,
                'Dharmadevi Municipality': 19
            },
            'Solukhumbu': {
                'Mahakulung Rural Municipality': 21,
                'Khumbu Pasanglhamu Rural Municipality': 20,
                'Solu Dudhkunda Municipality': 26,
                'Likhupike Rural Municipality': 27,
                'Nechasalyan Rural Municipality': 25,
                'Thulung Dudhkoshi Rural Municipality': 24,
                'Mapya Dudhkoshi Rural Municipality': 23,
                'Sotang Rural Municipality': 22
            },
            'Okhaldhunga': {
                'Chishankhugadhi Rural Municipality': 28,
                'Siddhicharan Municipality': 29,
                'Manebhanjyang Rural Municipality': 35,
                'Sunkoshi Rural Municipality': 34,
                'Molung Rural Municipality': 30,
                'Champadevi Rural Municipality': 33,
                'Khijidemba Rural Municipality': 31,
                'Likhu Rural Municipality': 32
            },
            'Udayapur': {
                'Belaka Municipality': 130,
                'Chaudandigadhi Municipality': 131,
                'Triyuga Municipality': 132,
                'Rautamai Rural Municipality': 133,
                'Udayapurgadhi Rural Municipality': 137,
                'limchungbung Rural Municipality': 134,
                'Tapli Rural Municipality': 135,
                'Katari Municipality': 136
            },
            'Sunsari': {
                'Barju Rural Municipality': 129,
                'Dewangunj Rural Municipality': 128,
                'Harinagar Rural Municipality': 127,
                'Gadhi Rural Municipality': 125,
                'Duhabi Municipality': 124,
                'Itahari Sub-Metropolitan City': 123,
                'Dharan Sub-Metropolitan City': 118,
                'Barahakshetra Municipality': 119,
                'Koshi Rural Municipality': 120,
                'Bhokraha Narsingh Rural Municipality': 121,
                'Inaruwa Municipality': 126,
                'Gadhi Rural Municipality': 125

            },
            'Morang': {
                'Biratnagar Metropolitan': 114,
                'Jahada Rural Municipality': 117,
                'Dhanpalthan Rural Municipality': 116,
                'Rangeli Municipality': 111,
                'Sunbarsi Municipality': 110,
                'Ratuwamai Municipality': 109,
                'Katahari Rural Municipality': 115,
                'Urlabari Municipality': 108,
                'Pathari Shanishchare Municipality': 107,
                'Kanepokhari Rural Municipality': 106,
                'Belbari Municipality': 105,
                'Sundarharaincha Municipality': 104,
                'Gramthan Rural Municipality': 112,
                'Budhiganga Rural Municipality': 113,
                'Miklajung Rural Municipality': 101,
                'Letang Municipality': 102,
                'Kerabari Rural Municipality': 103

            },
            'Jhapa': {
                'Gaurigunj Rural Municipality': 94,
                'Jhapa Rural Municipality': 95,
                'Bahradashi Rural Municipality': 96,
                'Haldibari Rural Municipality': 98,
                'Bhadrapur Municipality': 99,
                'Kachankawal Rural Municipality': 100,
                'Gauradaha Municipality': 93,
                'Kamal Rural Municipality': 91,
                'Damak Municipality': 92,
                'Shivasatakshi Municipality': 90,
                'Kankai Municipality': 89,
                'Birtamod Municipality': 97,
                'Mechinagar Municipality': 86,
                'Buddhashanti Rural Municipality': 87,
                'Arjundhara Municipality': 88
            },
            'Ilam': {
                'Chulachuli Rural Municipality': 82,
                'Mai Municipality': 83,
                'Suryodaya Municipality': 84,
                'Rong Rural Municipality': 85,
                'Maijogmai Rural Municipality': 76,
                'Ilam Municipality': 78,
                'Deumai Municipality': 79,
                'Mangsebung Rural Municipality': 81,
                'Phakphokthum Rural Municipality': 80,
                'Sandakpur Rural Municipality': 77

            },
            'Panchthar': {
                'Miklajung Rural Municipality': 75,
                'Tumbewa Rural Municipality': 74,
                'Kummayak Rural Municipality': 73,
                'Phalgunanda Rural Municipality': 72,
                'Phidim Municipality': 71,
                'Phalelung Rural Municipality': 70,
                'Yangwarak Rural Municipality': 68,
                'Hilihang Rural Municipality': 69
            },
            'Tehrathum': {
                'Chhathar Rural Municipality': 67,
                'Laligurans Municipality': 66,
                'Myanglung Municipality': 65,
                'Phedap Rural Municipality': 63,
                'Aatharai Rural Municipality': 62,
                'Menchhayayem Rural Municipality': 64
            },
            'Dhankuta': {
                'Chaubise Rural Municipality': 61,
                'Sangurigadhi Rural Municipality': 60,
                'Chhathar Jorpati Rural Municipality': 57,
                'Dhankuta Municipality': 58,
                'Shahidbhumi Rural Municipality': 59,
                'Pakhribas Municipality': 56,
                'Mahalaxmi Municipality': 55
            },
            'Bhojpur': {
                'Aamchok Rural Municipality': 54,
                'Hatuwagadhi Rural Municipality': 53,
                'Ramprasad Rai Rural Municipality': 52,
                'Pauwadungma Rural Municipality': 51,
                'Arun Rural Municipality': 50,
                'Bhojpur Municipality': 49,
                'Temkemaiyung Rural Municipality': 48,
                'Sadananda Municipality': 46,
                'Salpasilichho Rural Municipality': 47
            },
            'Khotang': {
                'Barahapokhari Rural Municipality': 45,
                'Jantedhunga Rural Municipality': 44,
                'Khotehang Rural Municipality': 43,
                'Diprung Chuichumma Rural Municipality': 42,
                'Sakela Rural Municipality': 41,
                'Diktel Rupakot Majhuwagadhi Municipality': 40,
                'Halesi Tuwachung Municipality': 39,
                'Rawabesi Rural Municipality': 38,
                'Kepilasgadhi Rural Municipality': 36,
                'Ainselukharka Rural Municipality': 37
            },
        },
        'Madhesh': {
            'Saptari': {
                'Saptakoshi Municipality': 138,
                'Kanchanrup Municipality': 139,
                'Agnisair Krishnasawaran Rural Municipality': 140,
                'Rupani Rural Municipality': 141,
                'Shambhunath Municipality': 142,
                'Khadak Municipality': 143,
                'Surunga Municipality': 144,
                'Balanbihul Rural Municipality': 145,
                'Bodebarsain Municipality': 146,
                'Dakneshwori Municipality': 147,
                'Rajgadh Rural Municipality': 148,
                'Bishnupur Rural Municipality': 149,
                'Rajbiraj Municipality': 150,
                'Mahadeva Rural Municipality': 151,
                'Tirahut Rural Municipality': 152,
                'Hanumannagar Kankalini Municipality': 153,
                'Tilathi Koiladi Rural Municipality': 154,
                'Chhinnamasta Rural Municipality': 155
            },

            'Siraha': {
                'Bhagwanpur Rural Municipality': 168,
                'Sakhuwa Nankarkatti Rural Municipality': 167,
                'Navarajpur Rural Municipality': 169,
                'Bariyarpatti Rural Municipality': 170,
                'Laxmipur Patari Rural Municipality': 166,
                'Sukhipur Municipality': 165,
                'Aurahi Rural Municipality': 171,
                'Arnama Rural Municipality': 164,
                'Siraha Municipality': 172,
                'Golbazar Municipality': 158,
                'Bishnupur Rural Municipality': 163,
                'Naraha Rural Municipality': 162,
                'Kalyanpur Municipality': 161,
                'Mirchaiya Municipality': 159,
                'Karjanha Municipality': 160,
                'Dhangadhimai Municipality': 157,
                'Lahan Municipality': 156
            },
            'Dhanusa': {
                'Janaknandini Rural Municipality': 184,
                'Kamala Municipality': 183,
                'Bideha Municipality': 185,
                'Shahidnagar Municipality': 182,
                'Sabaila Municipality': 181,
                'Hansapur Municipality': 180,
                'Aurahi Rural Municipality': 186,
                'Dhanauji Rural Municipality': 188,
                'Nagarain Municipality': 189,
                'Mukhiyapatti Musaharmiya Rural Municipality': 190,
                'Janakpurdham Sub-Metropolitan City': 187,
                'Mithila Bihari Municipality': 179,
                'Laxminiya Rural Municipality': 178,
                'Kshireshwornath Municipality': 177,
                'Dhanusadham Municipality': 174,
                'Ganeshman Charnath Municipality': 173,
                'Mithila Municipality': 175
            },

            'Mahottari': {
                'Matihani Municipality': 204,
                'Jaleshwor Municipality': 205,
                'Pipara Rural Municipality': 203,
                'Mahottari Rural Municipality': 202,
                'Ekdara Rural Municipality': 201,
                'Manara Shiswa Municipality': 200,
                'Loharpatti Municipality': 196,
                'Balawa Municipality': 197,
                'Ramgopalpur Municipality': 198,
                'Samsi Rural Municipality': 199,
                'Bhangaha Municipality': 195,
                'Aurahi Municipality': 194,
                'Sonma Rural Municipality': 193,
                'Gaushala Municipality': 192,
                'Bardibas Municipality': 191


            },

            'Sarlahi': {
                'Balara Municipality': 221,
                'Ramnagar Rural Municipality': 220,
                'Bishnu Rural Municipality': 223,
                'Godaita Municipality': 222,
                'Dhanakaul Rural Municipality': 219,
                'Malangawa Municipality': 225,
                'Kaudena Rural Municipality': 224,
                'Chakraghatta Rural Municipality': 217,
                'Basbariya Rural Municipality': 218,
                'Barahathawa Municipality': 209,
                'Kabilasi Municipality': 216,
                'Chandranagar Rural Municipality': 215,
                'Brahmapuri Rural Municipality': 214,
                'Parsa Rural Municipality': 213,
                'Haripurwa Municipality': 212,
                'Ishworpur Municipality': 211,
                'Lalbandi Municipality': 206,
                'Hariwan Municipality': 207,
                'Haripur Municipality': 210,
                'Bagmati Municipality': 208



            },
            'Rautahat': {
                'Rajdevi Municipality': 241,
                'Gaur Municipality': 242,
                'Ishnath Municipality': 243,
                'Rajpur Municipality': 238,
                'Yamunamai Rural Municipality': 239,
                'Durgabhagawati Rural Municipality': 240,
                'Paroha Municipality': 237,
                'Madhavnarayan Municipality': 232,
                'Gadhimai Municipality': 231,
                'Brindaban Municipality': 230,
                'Chandrapur Municipality': 226,
                'Gujara Municipality': 227,
                'Phatuwa Bijayapur Municipality': 228,
                'Katahariya Municipality': 229,
                'Maulapur Municipality':  235,
                'Baudhimai Municipality': 236,
                'Dewahi Gonahi Municipality': 234,
                'Garuda Municipality': 233,
            },

            'Bara': {
                'Pachrauta Municipality': 256,
                'Simraungadh Municipality': 255,
                'Aadarsha Kotwal Rural Municipality': 254,
                'Suvarna Rural Municipality': 259,
                'Devtal Rural Municipality': 258,
                'Mahagadhimai Municipality': 257,
                'Baragadhi Rural Municipality': 253,
                'Karaiyamai Rural Municipality': 252,
                'Kalaiya Sub-Metropolitan City': 251,
                'Pheta Rural Municipality': 250,
                'Bishrampur Rural Municipality': 249,
                'Prasauni Rural Municipality': 248,
                'Parwanipur Rural Municipality': 247,
                'Kolhawi Municipality': 245,
                'Nijgadh Municipality': 244,
                'Jitpur Simra Sub-Metropolitan City': 246

            },
            'Parsa': {
                'Birgunj Metropolitan': 266,
                'Parsagadhi Municipality': 265,
                'Bahudarmai Municipality': 267,
                'Bindabasini Rural Municipality': 273,
                'Pakaha Mainpur Rural Municipality': 272,
                'Pokhariya Municipality': 268,
                'Sakhuwa Prasauni Rural Municipality': 264,
                'Paterwa Sugauli Rural Municipality': 263,
                'Dhobini Rural Municipality': 270,
                'Chhipaharmai Rural Municipality': 271,
                'Jagarnathpur Rural Municipality': 262,
                'Jirabhawani Rural Municipality': 261,
                'Thori Rural Municipality': 260,
                'Kalikamai Rural Municipality': 269

            }

        },
        'Bagmati': {
            'Sindhuli': {
                'Dudhauli Municipality': 367,
                'Tinpatan Rural Municipality': 369,
                'Phikkal Rural Municipality': 368,
                'Golanjor Rural Municipality': 370,
                'Kamalamai Municipality': 371,
                'Sunkoshi Rural Municipality': 372,
                'Ghyanglekh Rural Municipality': 373,
                'Marin Rural Municipality': 374,
                'Hariharpurgadhi Rural Municipality': 375
            },
            'Ramechhap': {
                'Umakunda Rural Municipality': 359,
                'Gokulganga Rural Municipality': 360,
                'Likhu Tamakoshi Rural Municipality': 361,
                'Ramechhap Municipality': 362,
                'Manthali Municipality': 363,
                'Khandadevi Rural Municipality': 364,
                'Doramba Rural Municipality': 365,
                'Sunapati Rural Municipality': 366
            },
            'Dolakha': {
                'Gaurishankar Rural Municipality': 274,
                'Jiri Municipality': 278,
                'Bigu Rural Municipality': 275,
                'Kalinchok Rural Municipality': 276,
                'Bhimeshwor Municipality': 282,
                'Baiteshwor Rural Municipality': 277,
                'Shailung Rural Municipality': 281,
                'Melung Rural Municipality': 280,
                'Tamakoshi Rural Municipality': 279

            },
            'Sindhupalchok': {
                'Helambu Rural Municipality': 286,
                'Panchpokhari Thangpal Rural Municipality': 285,
                'Jugal Rural Municipality': 284,
                'Bhotekoshi Rural Municipality': 283,
                'Bahrabise Municipality': 291,
                'Tripurasundari Rural Municipality': 292,
                'Lisankhupakhar Rural Municipality': 293,
                'Sunkoshi Rural Municipality': 294,
                'Balephi Rural Municipality': 290,
                'Chautara Sangachokgadhi Municipality': 289,
                'Indrawati Rural Municipality': 288,
                'Melamchi Municipality': 287
            },
            'Kavrepalanchok': {
                'Mandan Deupur Municipality': 348,
                'Bhumlu Rural Municipality': 347,
                'Chauri Deurali Rural Municipality': 346,
                'Temal Rural Municipality': 352,
                'Panchkhal Municipality': 351,
                'Banepa Municipality': 349,
                'Dhulikhel Municipality': 350,
                'Namobuddha Municipality': 353,
                'Roshi Rural Municipality': 356,
                'Bethanchok Rural Municipality': 355,
                'Panauti Municipality': 354,
                'Khanikhola Rural Municipality': 358,
                'Mahabharat Rural Municipality': 357
            },
            'Rasuwa': {
                'Gosainkunda Rural Municipality': 295,
                'Parbatikunda Rural Municipality': 296,
                'Naukunda Rural Municipality': 299,
                'Kalika Rural Municipality': 298,
                'Uttargaya Rural Municipality': 297
            },
            'Nuwakot': {
                'Shivapuri Rural Municipality': 323,
                'Dupcheshwor Rural Municipality': 313,
                'Tadi Rural Municipality': 314,
                'Panchakanya Rural Municipality': 322,
                'Kakani Rural Municipality': 324,
                'Likhu Rural Municipality': 321,
                'Suryagadhi Rural Municipality': 315,
                'Belkotgadhi Municipality': 320,
                'Bidur Municipality': 316,
                'Kispang Rural Municipality': 317,
                'Myagang Rural Municipality': 318,
                'Tarakeshwor Rural Municipality': 319,

            },

            'Dhading': {
                'Dhunibesi Municipality': 312,
                'Thakre Rural Municipality': 311,
                'Galchhi Rural Municipality': 310,
                'Gajuri Rural Municipality': 309,
                'Benighat Rorang Rural Municipality': 308,
                'Siddhalek Rural Municipality': 307,
                'Nilkantha Municipality': 305,
                'Jwalamukhi Rural Municipality': 306,
                'Netrawati Dabjong Rural Municipality': 304,
                'Tripurasundari Rural Municipality': 303,
                'Gangajamuna Rural Municipality': 302,
                'Khaniyabas Rural Municipality': 301,
                'Rubivalley Rural Municipality': 300
            },
            'Chitwan': {
                'Madi Municipality': 392,
                'Rapti Municipality': 386,
                'Khairahani Municipality': 391,
                'Ratnanagar Municipality': 390,
                'Bharatpur Metropolitan': 389,
                'Kalika Municipality': 387,
                'Ichchhakamana Rural Municipality': 388
            },
            'Makwanpur': {
                'Bagmati Rural Municipality': 385,
                'Bakaiya Rural Municipality': 384,
                'Hetaunda Sub-Metropolitan City': 381,
                'Makwanpurgadhi Rural Municipality': 383,
                'Bhimphedi Rural Municipality': 382,
                'Indrasarowar Rural Municipality': 376,
                'Thaha Municipality': 377,
                'Kailash Rural Municipality': 378,
                'Raksirang Rural Municipality': 379,
                'Manahari Rural Municipality': 380
            },
            'Lalitpur': {
                'Mahankal Rural Municipality': 344,
                'Bagmati Rural Municipality': 345,
                'Konjyosom Rural Municipality': 343,
                'Godawari Municipality': 342,
                'Mahalaxmi Municipality': 340,
                'Lalitpur Metropolitan': 341
            },
            'Bhaktapur': {
                'Suryabinayak Municipality': 339,
                'Changunarayan Municipality': 336,
                'Bhaktapur Municipality': 337,
                'Madhyapur Thimi Municipality': 338
            },
            'Kathmandu': {
                'Dakshinkali Municipality': 335,
                'Kirtipur Municipality': 333,
                'Chandragiri Municipality': 334,
                'Nagarjun Municipality': 331,
                'Kathmandu Metropolitan': 332,
                'Tarakeshwor Municipality': 330,
                'Tokha Municipality': 329,
                'Budhanilkantha Municipality': 328,
                'Gokarneshwor Municipality': 327,
                'Kageshwori Manohara Municipality': 326,
                'Shankharapur Municipality': 325
            }
        },
        'Gandaki': {
            'Nawalparasi East': {
                'Binayi Triveni Rural Municipality': 449,
                'Madhyabindu Municipality': 448,
                'Kawasoti Municipality': 447,
                'Hupsekot Rural Municipality': 445,
                'Devchuli Municipality': 446,
                'Gaindakot Municipality': 442,
                'Bulingtar Rural Municipality': 443,
                'Baudikali Rural Municipality': 444

            },
            'Tanahun': {
                'Devghat Rural Municipality': 439,
                'Aanbukhaireni Rural Municipality': 441,
                'Bandipur Rural Municipality': 440,
                'Rishing Rural Municipality': 438,
                'Byas Municipality': 433,
                'Bhanu Municipality': 432,
                'Ghiring Rural Municipality': 437,
                'Myagde Rural Municipality': 434,
                'Bhimad Municipality': 436,
                'Shuklagandaki Municipality': 435

            },
            'Gorkha': {
                'Gandaki Rural Municipality': 403,
                'Shahid Lakhan Rural Municipality': 402,
                'Bhimsen Thapa Rural Municipality': 398,
                'Gorkha Municipality': 401,
                'Palungtar Municipality': 400,
                'Siranchok Rural Municipality': 399,
                'Barpak Sulikot Rural Municipality':  395,
                'Aarughat Rural Municipality': 397,
                'Ajirkot Rural Municipality': 394,
                'Dharche Rural Municipality': 396,
                'Chumnubri Rural Municipality': 393
            },
            'Lamjung': {
                'Rainas Municipality': 430,
                'Dudhpokhari Rural Municipality': 431,
                'Dordi Rural Municipality': 424,
                'Besishahar Municipality': 428,
                'Sundarbazar Municipality': 429,
                'Kwholasothar Rural Municipality': 426,
                'Marsyangdi Rural Municipality': 425,
                'Madhyanepal Municipality': 427
            },
            'Syangja': {
                'Kaligandaki Rural Municipality': 460,
                'Galyang Municipality': 459,
                'Waling Municipality': 458,
                'Chapakot Municipality': 457,
                'Harinas Rural Municipality': 456,
                'Biruwa Rural Municipality': 455,
                'Bhirkot Municipality': 454,
                'Putalibazar Municipality': 450,
                'Phedikhola Rural Municipality': 451,
                'Aandhikhola Rural Municipality': 452,
                'Arjunchaupari Rural Municipality': 453
            },
            'Kaski': {
                'Rupa Rural Municipality': 423,
                'Pokhara Metropolitan': 422,
                'Madi Rural Municipality': 419,
                'Machhapuchchhre Rural Municipality': 420,
                'Annapurna Rural Municipality': 421
            },
            'Manang': {
                'Nason Rural Municipality': 407,
                'Chame Rural Municipality': 406,
                'Narpabhumi Rural Municipality': 404,
                'Manang Ngisyang Rural Municipality': 405
            },
            'Mustang': {
                'Thasang Rural Municipality': 412,
                'Gharpajhong Rural Municipality': 409,
                'Baragung Muktikshetra Rural Municipality': 410,
                'Lo-Ghekar Damodarkunda Rural Municipality': 408,
                'Lomanthang Rural Municipality': 411
            },
            'Myagdi': {
                'Annapurna Rural Municipality': 413,
                'Raghuganga Rural Municipality': 414,
                'Mangala Rural Municipality': 417,
                'Beni Municipality': 418,
                'Malika Rural Municipality': 416,
                'Dhawalagiri Rural Municipality': 415
            },
            'Baglung': {
                'Jaimini Municipality': 477,
                'Baglung Municipality': 468,
                'Kathekhola Rural Municipality': 469,
                'Bareng Rural Municipality': 476,
                'Galkot Municipality': 475,
                'Tarakhola Rural Municipality': 470,
                'Badigad Rural Municipality': 474,
                'Nisikhola Rural Municipality': 473,
                'Dhorpatan Municipality': 472,
                'Tamankhola Rural Municipality': 471,
            },

            'Parbat': {
                'Bihadi Rural Municipality': 466,
                'Paiyun Rural Municipality': 467,
                'Mahashila Rural Municipality': 465,
                'Phalebas Municipality': 464,
                'Kushma Municipality': 463,
                'Modi Rural Municipality': 461,
                'Jaljala Rural Municipality': 462
            }
        },
        'Lumbini': {
            'Arghakhanchi': {
                'Shitganga Municipality': 517,
                'Panini Rural Municipality': 516,
                'Chhatradev Rural Municipality': 512,
                'Sandhikharka Municipality': 515,
                'Bhumikasthan Municipality': 514,
                'Malarani Rural Municipality': 513
            },
            'Banke': {
                'Narainapur Rural Municipality': 578,
                'Rapti Sonari Rural Municipality': 571,
                'Duduwa Rural Municipality': 577,
                'Nepalgunj Sub-Metropolitan City': 576,
                'Janaki Rural Municipality': 575,
                'Khajura Rural Municipality': 574,
                'Baijanath Rural Municipality': 573,
                'Kohalpur Municipality': 572
            },

            'Bardiya': {
                'Badhaiyatal Rural Municipality': 586,
                'Bansgadhi Municipality': 579,
                'Gulariya Municipality': 585,
                'Barbardiya Municipality': 580,
                'Madhuban Municipality': 584,
                'Thakurbaba Municipality': 581,
                'Rajapur Municipality': 583,
                'Geruwa Rural Municipality': 582
            },

            'Dang': {
                'Rajpur Rural Municipality': 570,
                'Gadhawa Rural Municipality': 569,
                'Rapti Rural Municipality': 568,
                'Lamahi Municipality': 567,
                'Bangalachuli Rural Municipality': 561,
                'Ghorahi Sub-Metropolitan City': 562,
                'Tulsipur Sub-Metropolitan City': 563,
                'Dangisharan Rural Municipality': 566,
                'Shantinagar Rural Municipality': 564,
                'Babai Rural Municipality': 565
            },
            'Gulmi': {
                'Kaligandaki Rural Municipality': 500,
                'Satyawati Rural Municipality': 501,
                'Ruru Rural Municipality': 511,
                'Chhatrakot Rural Municipality': 510,
                'Gulmidarbar Rural Municipality': 509,
                'Chandrakot Rural Municipality': 502,
                'Musikot Municipality': 503,
                'Isma Rural Municipality': 504,
                'Resunga Municipality': 508,
                'Dhurkot Rural Municipality': 507,
                'Malika Rural Municipality': 505,
                'Madane Rural Municipality': 506
            },
            'Kapilbastu': {
                'Shuddhodan Rural Municipality': 560,
                'Mayadevi Rural Municipality': 559,
                'Banganga Municipality': 551,
                'Kapilbastu Municipality': 557,
                'Yashodhara Rural Municipality': 558,
                'Maharajgunj Municipality': 556,
                'Buddhabhumi Municipality': 552,
                'Shivaraj Municipality': 553,
                'Krishnanagar Municipality': 555,
                'Bijayanagar Rural Municipality': 554
            },
            'Nawalparasi West': {
                'Susta Rural Municipality': 534,
                'Pratappur Rural Municipality': 533,
                'Bardaghat Municipality': 528,
                'Sarawal Rural Municipality': 532,
                'Palhinandan Rural Municipality': 531,
                'Ramgram Municipality': 530,
                'Sunwal Municipality': 529
            },
            'Palpa': {
                'Nisdi Rural Municipality': 527,
                'Rampur Municipality': 518,
                'Purbakhola Rural Municipality': 519,
                'Rambha Rural Municipality': 520,
                'Mathagadhi Rural Municipality': 526,
                'Tinau Rural Municipality': 525,
                'Baganaskali Rural Municipality': 521,
                'Tansen Municipality': 522,
                'Ribdikot Rural Municipality': 523,
                'Rainadevi Chhahara Rural Municipality': 524

            },
            'Pyuthan': {
                'Sarumarani Rural Municipality': 499,
                'Airawati Rural Municipality': 498,
                'Mandavi Rural Municipality': 496,
                'Mallarani Rural Municipality': 497,
                'Swargadwari Municipality': 495,
                'Pyuthan Municipality': 494,
                'Jhimruk Rural Municipality': 493,
                'Naubahini Rural Municipality': 492,
                'Gaumukhi Rural Municipality': 491

            },
            'Rolpa': {
                'Runtigadhi Rural Municipality': 488,
                'Sunil Smriti Rural Municipality': 489,
                'Lungri Rural Municipality': 490,
                'Sunchhahari Rural Municipality': 481,
                'Thawang Rural Municipality': 482,
                'Parivartan Rural Municipality': 483,
                'Gangadev Rural Municipality': 484,
                'Triveni Rural Municipality': 486,
                'Madi Rural Municipality': 485,
                'Rolpa Municipality': 487,
            },
            'Rukum East': {
                'Bhume Rural Municipality': 480,
                'Putha Uttarganga Rural Municipality': 478,
                'Sisne Rural Municipality': 479
            },
            'Rupandehi': {
                'Marchawari Rural Municipality': 550,
                'Sammarimai Rural Municipality': 549,
                'Kotahimai Rural Municipality': 548,
                'Lumbini Sanskritik Municipality': 547,
                'Rohini Rural Municipality': 544,
                'Omsatiya Rural Municipality': 543,
                'Siddharthanagar Municipality': 545,
                'Mayadevi Rural Municipality': 546,
                'Gaidahawa Rural Municipality': 539,
                'Siyari Rural Municipality': 541,
                'Tilottama Municipality': 542,
                'Devdaha Municipality': 535,
                'Butwal Sub-Metropolitan City': 536,
                'Shuddhodan Rural Municipality': 540,
                'Kanchan Rural Municipality': 538,
                'Sainamaina Municipality': 537
            }
        },
        'Karnali': {
            'Dailekh': {
                'Gurans Rural Municipality': 633,
                'Dungeshwor Rural Municipality': 632,
                'Bhagawatimai Rural Municipality': 631,
                'Narayan Municipality': 630,
                'Dullu Municipality': 629,
                'Naumule Rural Municipality': 623,
                'Mahabu Rural Municipality': 624,
                'Bhairavi Rural Municipality': 625,
                'Chamunda Bindrasaini Municipality': 628,
                'Thantikandh Rural Municipality': 626,
                'Aathbis Municipality': 627
            },
            'Dolpa': {
                'Chharka Tangsong Rural Municipality': 594,
                'Kaike Rural Municipality': 593,
                'Dolpobuddha Rural Municipality': 587,
                'Thulibheri Municipality': 592,
                'Tripurasundari Municipality': 591,
                'Shey Phoksundo Rural Municipality': 588,
                'Jagadulla Rural Municipality': 589,
                'Mudkechula Rural Municipality': 590
            },
            'Humla': {
                'Chankheli Rural Municipality': 599,
                'Tanjakot Rural Municipality': 605,
                'Adanchuli Rural Municipality': 604,
                'Sarkegad Rural Municipality': 603,
                'Kharpunath Rural Municipality': 600,
                'Simkot Rural Municipality': 601,
                'Namkha Rural Municipality': 602,

            },
            'Jajarkot': {
                'Shivalaya Rural Municipality': 638,
                'Bheri Municipality': 639,
                'Chhedagad Municipality': 637,
                'Junichande Rural Municipality': 636,
                'Kushe Rural Municipality': 635,
                'Barekot Rural Municipality': 634,
                'Nalgad Municipality': 640
            },
            'Jumla': {
                'Patarasi Rural Municipality': 606,
                'Guthichaur Rural Municipality': 610,
                'Tatopani Rural Municipality': 611,
                'Chandannath Municipality': 609,
                'Tila Rural Municipality': 612,
                'Hima Rural Municipality': 613,
                'Sinja Rural Municipality': 608,
                'Kanakasundari Rural Municipality': 607
            },
            'Kalikot': {
                'Mahawai Rural Municipality': 621,
                'Tilagupha Municipality': 620,
                'Shuvakalika Rural Municipality': 622,
                'Khandachakra Municipality': 619,
                'Pachaljharna Rural Municipality': 615,
                'Palata Rural Municipality': 614,
                'Naraharinath Rural Municipality': 618,
                'Sanni Triveni Rural Municipality': 617,
                'Raskot Municipality': 616
            },
            'Mugu': {
                'Mugum Karmarong Rural Municipality': 595,
                'Chhayanath Rara Municipality': 596,
                'Soru Rural Municipality': 597,
                'Khatyad Rural Municipality': 598
            },
            'Rukum West': {
                'Triveni Rural Municipality': 645,
                'Musikot Municipality': 644,
                'Chaurjahari Municipality': 646,
                'Sanibheri Rural Municipality': 642,
                'Banphikot Rural Municipality': 643,
                'Aathbiskot Municipality': 641
            },
            'Salyan': {
                'Kalimati Rural Municipality': 654,
                'Triveni Rural Municipality': 655,
                'Kapurkot Rural Municipality': 656,
                'Chhatreshwori Rural Municipality': 652,
                'Sharada Municipality': 653,
                'Bangad Kupinde Municipality': 649,
                'Siddhakumakh Rural Municipality': 650,
                'Kumakh Rural Municipality': 648,
                'Darma Rural Municipality': 647,
                'Bagchaur Municipality': 651,
            },
            'Surkhet': {
                'Gurbhakot Municipality': 660,
                'Simta Rural Municipality': 657,
                'Chingad Rural Municipality': 658,
                'Lekbesi Municipality': 659,
                'Bheriganga Municipality': 661,
                'Birendranagar Municipality': 662,
                'Barahatal Rural Municipality': 663,
                'Panchapuri Municipality': 664,
                'Chaukune Rural Municipality': 665
            },

        },
        'Sudurpashchim': {
            'Achham': {
                'Turmakhand Rural Municipality': 731,
                'Dhakari Rural Municipality': 730,
                'Kamalbazar Municipality': 729,
                'Panchdeval Binayak Municipality': 722,
                'Mangalsen Municipality': 727,
                'Ramaroshan Rural Municipality': 723,
                'Bannigadhi Jayagadh Rural Municipality': 728,
                'Chaurpati Rural Municipality': 726,
                'Sanphebagar Municipality': 725,
                'Mellekh Rural Municipality': 724
            },
            'Baitadi': {
                'Sigas Rural Municipality': 705,
                'Patan Municipality': 704,
                'Surnaya Rural Municipality': 699,
                'Purchaudi Municipality': 698,
                'Dilasaini Rural Municipality': 696,
                'Dogadakedar Rural Municipality': 697,
                'Dasharath Chand Municipality': 700,
                'Pancheshwor Rural Municipality': 701,
                'Shivanath Rural Municipality': 702,
                'Melauli Municipality': 703,
            },
            'Bajhang': {
                'Saipal Rural Municipality': 675,
                'Talkot Rural Municipality': 678,
                'Masta Rural Municipality': 679,
                'Jayaprithvi Municipality': 680,
                'Khaptadchhanna Rural Municipality': 686,
                'Thalara Rural Municipality': 685,
                'Bitthadchir Rural Municipality': 684,
                'Kedarsyun Rural Municipality': 683,
                'Durgathali Rural Municipality': 682,
                'Chhabis Pathibhera Rural Municipality': 681,
                'Surma Rural Municipality': 677,
                'Bungal Municipality': 676
            },
            'Bajura': {
                'Himali Rural Municipality': 666,
                'Gaumul Rural Municipality': 667,
                'Budhinanda Municipality': 668,
                'Swamikartik Khapar Rural Municipality': 669,
                'Jagannath Rural Municipality': 670,
                'Triveni Municipality': 674,
                'Budhiganga Municipality': 673,
                'Khaptad Chhededaha Rural Municipality': 672,
                'Badimalika Municipality': 671,
            },
            'Dandeldhura': {
                'Parashuram Municipality': 710,
                'Aalital Rural Municipality': 711,
                'Ganyapdhura Rural Municipality': 712,
                'Navadurga Rural Municipality': 706,
                'Amargadhi Municipality': 707,
                'Bhageshwor Rural Municipality': 709,
                'Ajayameru Rural Municipality': 708
            },
            'Darchula': {
                'Vyans Rural Municipality': 687,
                'Apihimal Rural Municipality': 691,
                'Marma Rural Municipality': 692,
                'Naugad Rural Municipality': 690,
                'Duhun Rural Municipality': 688,
                'Mahakali Municipality': 689,
                'Malikarjun Rural Municipality': 694,
                'Lekam Rural Municipality': 695,
                'Shailyashikhar Municipality': 693
            },
            'Doti': {
                'Sayal Rural Municipality': 714,
                'Purbichauki Rural Municipality': 713,
                'Dipayal Silgadhi Municipality': 717,
                'Aadarsha Rural Municipality': 715,
                'Shikhar Municipality': 716,
                'K.I. Singh Rural Municipality': 718,
                'Jorayal Rural Municipality': 721,
                'Badikedar Rural Municipality': 720,
                'Bogatan Phudsil Rural Municipality': 719

            },
            'Kailali': {
                'Godawari Municipality': 734,
                'Chure Rural Municipality': 733,
                'Dhangadhi Sub-Metropolitan City': 744,
                'Gauriganga Municipality': 735,
                'Kailari Rural Municipality': 743,
                'Ghodaghodi Municipality': 736,
                'Mohanyal Rural Municipality': 732,
                'Lamkichuha Municipality': 738,
                'Janaki Rural Municipality': 739,
                'Tikapur Municipality': 741,
                'Bhajani Municipality': 742,
                'Bardgoriya Rural Municipality': 737,
                'Joshipur Rural Municipality': 740

            },
            'Kanchanpur': {
                'Dodharachandani Municipality': 749,
                'Bhimdatta Municipality': 748,
                'Bedkot Municipality': 747,
                'Shuklaphanta Municipality': 746,
                'Krishnapur Municipality': 745,
                'Laljhadi Rural Municipality': 750,
                'Punarbas Municipality': 751,
                'Belauri Municipality': 752,
                'Beldandi Rural Municipality': 753

            }
        }
    }
]

# for test
mappings = [
    {
        'Koshi': {
            'Taplejung': {
                'Phaktanglung Rural Municipality': 1,
                'Maiwakhola Rural Municipality': 2,
                'Meringden Rural Municipality': 3,
                'Maiwakhola Rural Municipality': 4,
                'Aathrai Triveni Rural Municipality': 5,
                'Phungling Municipality': 6,
                'Pathibhara Yangwarak Rural Municipality': 7,
                'Sirijangha Rural Municipality': 8,
                'Sidingwa Rural Municipality': 9

            }
        },
        'Madhesh': {
            'Saptari': {
                'Saptakoshi Municipality': 138,
                'Kanchanrup Municipality': 139,
                'Agnisair Krishnasawaran Rural Municipality': 140,
                'Rupani Rural Municipality': 141,
                'Shambhunath Municipality': 142,
                'Khadak Municipality': 143,
                'Surunga Municipality': 144,
                'Balanbihul Rural Municipality': 145,
                'Bodebarsain Municipality': 146,
                'Dakneshwori Municipality': 147,
                'Rajgadh Rural Municipality': 148,
                'Bishnupur Rural Municipality': 149,
                'Rajbiraj Municipality': 150,
                'Mahadeva Rural Municipality': 151,
                'Tirahut Rural Municipality': 152,
                'Hanumannagar Kankalini Municipality': 153,
                'Tilathi Koiladi Rural Municipality': 154,
                'Chhinnamasta Rural Municipality': 155
            }

        }

    }
]

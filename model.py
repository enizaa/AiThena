import pickle
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense

# define base model
def baseline_model(dim_shape):
    # create model
    model = Sequential()
    model.add(Dense(256, input_dim=dim_shape, kernel_initializer='normal', activation='relu'))
    
    model.add(Dense(128, kernel_initializer='normal', activation='relu'))
    model.add(Dense(128, kernel_initializer='normal', activation='relu'))
    model.add(Dense(128, kernel_initializer='normal', activation='relu'))
    
    model.add(Dense(1, kernel_initializer='normal', activation='linear'))
    
    # Compile model
    model.compile(loss='mae', 
                  optimizer='adam') 
    return model

import pickle
from keras.models import load_model

def load():
    model = load_model('model/model.h5')
    scaler = pickle.load(open('model/scaler.pkl', 'rb'))
    return model, scaler
    
def Merk(Merek):
    if Merek == 'Audi':
        result = 0
    elif Merek == 'BMW':
        result = 1
    elif Merek == 'Chevrolet':
        result = 2
    elif Merek == 'Daihatsu':
        result = 3
    elif Merek == 'Datsun':
        result = 4
    elif Merek == 'Ford':
        result = 5
    elif Merek == 'Hino':
        result = 6
    elif Merek == 'Honda':
        result = 7
    elif Merek == 'Hyundai':
        result = 8
    elif Merek == 'Isuzu':
        result = 9
    elif Merek == 'Jeep':
        result = 10
    elif Merek == 'KIA':
        result = 11
    elif Merek == 'Land Rover':
        result = 12
    elif Merek == 'Lexus':
        result = 13
    elif Merek == 'Mazda':
        result = 14
    elif Merek == 'Mercedes-Benz':
        result = 15
    elif Merek == 'Mini Cooper':
        result = 16
    elif Merek == 'Mitsubishi':
         result = 17
    elif Merek == 'Nissan':
        result = 18
    elif Merek == 'Peugeot':
        result = 19
    elif Merek == 'Porsche':
        result = 20
    elif Merek == 'Proton':
        result = 21
    elif Merek == 'Suzuki':
        result = 22
    elif Merek == 'Timor':
        result = 23
    elif Merek == 'Toyota':
        result = 24
    elif Merek == 'Volkswagen':
        result = 25
    elif Merek == 'Wuling':
        result = 26
    return    result

def MDl(Model):
    if Model == '120':
        result = 0
    elif Model == '2':
        result = 1
    elif Model == '206':
        result = 2
    elif Model == '207':
        result = 3
    elif Model == '3':
        result = 4
    elif Model == '3008':
        result = 5
    elif Model == '306':
        result = 6
    elif Model == '307':
        result = 7
    elif Model == '308':
        result = 8
    elif Model == '323':
        result = 9
    elif Model == '405':
        result = 10
    elif Model == '406':
        result = 11
    elif Model == '407':
        result = 12
    elif Model == '408':
        result = 13
    elif Model == '430':
        result = 14
    elif Model == '5':
        result = 15
    elif Model == '505':
        result = 16
    elif Model == '6':
        result = 17
    elif Model == '620':
        result = 18
    elif Model == '626':
        result = 19
    elif Model == '8':
        result = 20
    elif Model == '806':
        result = 21
    elif Model == '807':
        result = 22
    elif Model == '86':
        result = 23
    elif Model == '911':
        result = 24
    elif Model == 'A-Class':
        result = 25
    elif Model == 'APV':
        result = 26
    elif Model == 'Accent':
        result = 27
    elif Model == 'Accord':
        result = 28
    elif Model == 'Aerio':
        result = 29
    elif Model == 'Agya':
        result = 30
    elif Model == 'Allroad':
        result = 31
    elif Model == 'Alphard':
        result = 32
    elif Model == 'Altis':
        result = 33
    elif Model == 'Amenity':
        result = 34
    elif Model == 'Astina':
        result = 35
    elif Model == 'Atoz':
        result = 36
    elif Model == 'Audi A3':
        result = 37
    elif Model == 'Audi A4':
        result = 38
    elif Model == 'Audi A5':
        result = 39
    elif Model == 'Audi A6':
        result = 40
    elif Model == 'Audi A8':
        result = 41
    elif Model == 'Audi Q3':
        result = 42
    elif Model == 'Audi Q7':
        result = 43
    elif Model == 'Audi S5':
        result = 44
    elif Model == 'Audi TT':
        result = 45
    elif Model == 'Avanza':
        result = 46
    elif Model == 'Avega':
        result = 47
    elif Model == 'Aveo':
        result = 48
    elif Model == 'Ayla':
        result = 49
    elif Model == 'B-Class':
        result = 50
    elif Model == 'BR-V':
        result = 51
    elif Model == 'BT-50':
        result = 52
    elif Model == 'Baby Boomer':
        result = 53
    elif Model == 'Baleno':
        result = 54
    elif Model == 'Baleno next-G':
        result = 55
    elif Model == 'Beetle':
        result = 56
    elif Model == 'Biante':
        result = 57
    elif Model == 'Bighorn':
        result = 58
    elif Model == 'Blazer':
        result = 59
    elif Model == 'Boxster':
        result = 60
    elif Model == 'Brio':
        result = 61
    elif Model == 'C-Class':
        result = 62
    elif Model == 'CJ7':
        result = 63
    elif Model == 'CLA-Class':
        result = 64
    elif Model == 'CLC-Class':
        result = 65
    elif Model == 'CLK':
        result = 66
    elif Model == 'CLS':
        result = 67
    elif Model == 'CLS 350':
        result = 68
    elif Model == 'CLS-Class':
        result = 69
    elif Model == 'CR-V':
        result = 70
    elif Model == 'CR-Z':
        result = 71
    elif Model == 'CX-3':
        result = 72
    elif Model == 'CX-5':
        result = 73
    elif Model == 'CX-7':
        result = 74
    elif Model == 'CX-9':
        result = 75
    elif Model == 'Cakra':
        result = 76
    elif Model == 'Calya':
        result = 77
    elif Model == 'Camry':
        result = 78
    elif Model == 'Captiva':
        result = 79
    elif Model == 'Caravelle':
        result = 80
    elif Model == 'Carens I':
        result = 81
    elif Model == 'Carens II':
        result = 82
    elif Model == 'Carnival':
        result = 83
    elif Model == 'Carry':
        result = 84
    elif Model == 'Carry Pick-Up':
        result = 85
    elif Model == 'Carry Van':
        result = 86
    elif Model == 'Cayenne':
        result = 87
    elif Model == 'Cayman':
        result = 88
    elif Model == 'Ceria':
        result = 89
    elif Model == 'Charade':
        result = 90
    elif Model == 'Cherokee':
        result = 91
    elif Model == 'City':
        result = 92
    elif Model == 'Civic':
        result = 93
    elif Model == 'Classy':
        result = 94
    elif Model == 'Colorado':
        result = 95
    elif Model == 'Colt':
        result = 96
    elif Model == 'Colt 77 PS':
        result = 97
    elif Model == 'Combi':
        result = 98
    elif Model == 'Confero S':
        result = 99
    elif Model == 'Corolla':
        result = 100
    elif Model == 'Corolla Altis':
        result = 101
    elif Model == 'Corona':
        result = 102
    elif Model == 'Cortez':
        result = 103
    elif Model == 'Coupe':
        result = 104
    elif Model == 'Cross':
        result = 105
    elif Model == 'Cruze':
        result = 106
    elif Model == 'D-Max':
        result = 107
    elif Model == 'DOHC':
        result = 108
    elif Model == 'Defender':
        result = 109
    elif Model == 'Delica':
        result = 110
    elif Model == 'Discovery':
        result = 111
    elif Model == 'Discovery Sport':
        result = 112
    elif Model == 'Dutro':
        result = 113
    elif Model == 'E-Class':
        result = 114
    elif Model == 'E2000':
        result = 115
    elif Model == 'ES':
        result = 116
    elif Model == 'ES300':
        result = 117
    elif Model == 'Ecosport':
        result = 118
    elif Model == 'Elantra':
        result = 119
    elif Model == 'Elf Minibus':
        result = 120
    elif Model == 'Elgrand':
        result = 121
    elif Model == 'Ertiga':
        result = 122
    elif Model == 'Escape':
        result = 123
    elif Model == 'Escort':
        result = 124
    elif Model == 'Escudo':
        result = 125
    elif Model == 'Espass':
        result = 126
    elif Model == 'Estate':
        result = 127
    elif Model == 'Esteem':
        result = 128
    elif Model == 'Estilo':
        result = 129
    elif Model == 'Eterna':
        result = 130
    elif Model == 'Etios':
        result = 131
    elif Model == 'Etios Valco':
        result = 132
    elif Model == 'Evalia':
        result = 133
    elif Model == 'Everest':
        result = 134
    elif Model == 'Excel':
        result = 135
    elif Model == 'Exora':
        result = 136
    elif Model == 'FL235 JN':
        result = 137
    elif Model == 'Fairlady':
        result = 138
    elif Model == 'Familia':
        result = 139
    elif Model == 'Ferio':
        result = 140
    elif Model == 'Feroza':
        result = 141
    elif Model == 'Fiesta':
        result = 142
    elif Model == 'Focus':
        result = 143
    elif Model == 'Forsa':
        result = 144
    elif Model == 'Fortuner':
        result = 145
    elif Model == 'Free Lander':
        result = 146
    elif Model == 'Freed':
        result = 147
    elif Model == 'Futura':
        result = 148
    elif Model == 'G-Class':
        result = 149
    elif Model == 'GL-Class':
        result = 150
    elif Model == 'GLA-Class':
        result = 151
    elif Model == 'GLC-Class':
        result = 152
    elif Model == 'GLE-Class':
        result = 153
    elif Model == 'GLS-Class':
        result = 154
    elif Model == 'GS':
        result = 155
    elif Model == 'Gala':
        result = 156
    elif Model == 'Galant':
        result = 157
    elif Model == 'Gen2':
        result = 158
    elif Model == 'Genio':
        result = 159
    elif Model == 'Getz':
        result = 160
    elif Model == 'Go':
        result = 161
    elif Model == 'Go+':
        result = 162
    elif Model == 'Golf':
        result = 163
    elif Model == 'Gran Max':
        result = 164
    elif Model == 'Gran Max Pick-Up':
        result = 165
    elif Model == 'Grand Avega':
        result = 166
    elif Model == 'Grand Cherokee':
            result = 167
    elif Model == 'Grand Escudo':
        result = 168
    elif Model == 'Grand Livina':
        result = 169
    elif Model == 'Grand Touring':
        result = 170
    elif Model == 'Grand Vitara':
        result = 171
    elif Model == 'Grandis':
        result = 172
    elif Model == 'H-1':
        result = 173
    elif Model == 'H-100':
        result = 174
    elif Model == 'HI Ace':
        result = 175
    elif Model == 'HIJET':
        result = 176
    elif Model == 'HILUX':
        result = 177
    elif Model == 'HR-V':
        result = 178
    elif Model == 'Hardtop':
        result = 179
    elif Model == 'Harrier':
        result = 180
    elif Model == 'IS':
        result = 181
    elif Model == 'Ignis':
        result = 182
    elif Model == 'Innova':
        result = 183
    elif Model == 'Jazz':
        result = 184
    elif Model == 'Jeep':
        result = 185
    elif Model == 'Jimnie':
        result = 186
    elif Model == 'Jimny':
        result = 187
    elif Model == 'Juke':
        result = 188
    elif Model == 'Kalos':
        result = 189
    elif Model == 'Karimun':
        result = 190
    elif Model == 'Karimun Estillo':
        result = 191
    elif Model == 'Katana':
        result = 192
    elif Model == 'Kijang':
        result = 193
    elif Model == 'Kijang Pick-Up':
        result = 194
    elif Model == 'Kodok':
        result = 195
    elif Model == 'Kuda':
        result = 196
    elif Model == 'L200':
        result = 197
    elif Model == 'L300':
        result = 198
    elif Model == 'LS':
        result = 199
    elif Model == 'LX':
        result = 200
    elif Model == 'Lain-lain':
        result = 201
    elif Model == 'Lainnya':
        result = 202
    elif Model == 'Lancer':
        result = 203
    elif Model == 'Lancer Evolution':
        result = 204
    elif Model == 'Land Cruiser':
        result = 205
    elif Model == 'Lantis':
        result = 206
    elif Model == 'Latio':
        result = 207
    elif Model == 'Limo':
        result = 208
    elif Model == 'Livina':
        result = 209
    elif Model == 'Luxio':
        result = 210
    elif Model == 'Lynx':
        result = 211
    elif Model == 'M Series':
        result = 212
    elif Model == 'M-Class':
        result = 213
    elif Model == 'ML 350':
        result = 214
    elif Model == 'ML-Class':
        result = 215
    elif Model == 'MPV':
        result = 216
    elif Model == 'MR-90':
        result = 217
    elif Model == 'MU-X':
        result = 218
    elif Model == 'MX':
        result = 219
    elif Model == 'Maestro':
        result = 220
    elif Model == 'March':
        result = 221
    elif Model == 'Matrix':
        result = 222
    elif Model == 'Maven':
        result = 223
    elif Model == 'Mini Cooper':
        result = 224
    elif Model == 'Mirage':
        result = 225
    elif Model == 'Mobilio':
        result = 226
    elif Model == 'Montera':
        result = 227
    elif Model == 'Mustang':
        result = 228
    elif Model == 'NX':
        result = 229
    elif Model == 'Navara':
        result = 230
    elif Model == 'Neo':
        result = 231
    elif Model == 'Neo Baleno':
        result = 232
    elif Model == 'Neo Zebra':
        result = 233
    elif Model == 'New Panther':
        result = 234
    elif Model == 'New Tucson':
        result = 235
    elif Model == 'Odyssey':
        result = 236
    elif Model == 'Optima':
        result = 237
    elif Model == 'Optra':
        result = 238
    elif Model == 'Orlando':
        result = 239
    elif Model == 'Outlander':
        result = 240
    elif Model == 'Pajero':
        result = 241
    elif Model == 'Pajero Sport':
        result = 242
    elif Model == 'Panther':
        result = 243
    elif Model == 'Picanto':
        result = 244
    elif Model == 'Polo':
        result = 245
    elif Model == 'Pregio':
        result = 246
    elif Model == 'Prestige':
        result = 247
    elif Model == 'Pride':
        result = 248
    elif Model == 'R-Class':
        result = 249
    elif Model == 'R260':
        result = 250
    elif Model == 'RAV4':
        result = 251
    elif Model == 'RCZ':
        result = 252
    elif Model == 'RX':
        result = 253
    elif Model == 'RX-8':
        result = 254
    elif Model == 'Range Rover Evoque':
        result = 255
    elif Model == 'Range Rover Sport':
        result = 256
    elif Model == 'Range rover':
        result = 257
    elif Model == 'Ranger':
        result = 258
    elif Model == 'Renegade':
        result = 259
    elif Model == 'Rio':
        result = 260
    elif Model == 'Rio 5 Door':
        result = 261
    elif Model == 'Rocky':
        result = 262
    elif Model == 'Rubicon':
        result = 263
    elif Model == 'Rush':
        result = 264
    elif Model == 'S-Class':
        result = 265
    elif Model == 'S515i':
        result = 266
    elif Model == 'SL':
        result = 267
    elif Model == 'SLK':
        result = 268
    elif Model == 'SLK-Class':
        result = 269
    elif Model == 'SLS AMG':
        result = 270
    elif Model == 'SOHC':
        result = 271
    elif Model == 'SX4':
        result = 272
    elif Model == 'Safari':
        result = 273
    elif Model == 'Saga':
        result = 274
    elif Model == 'Sahara':
        result = 275
    elif Model == 'Santa Fe':
        result = 276
    elif Model == 'Satria':
        result = 277
    elif Model == 'Savvy':
        result = 278
    elif Model == 'Scirocco':
        result = 279
    elif Model == 'Sedona':
        result = 280
    elif Model == 'Sentra':
        result = 281
    elif Model == 'Serena':
        result = 282
    elif Model == 'Serie 1':
        result = 283
    elif Model == 'Serie 2':
        result = 284
    elif Model == 'Serie 3':
        result = 285
    elif Model == 'Serie 4':
        result = 286
    elif Model == 'Serie 5':
        result = 287
    elif Model == 'Serie 6':
        result = 288
    elif Model == 'Serie 7':
        result = 289
    elif Model == 'Shuma':
        result = 290
    elif Model == 'Sidekick':
        result = 291
    elif Model == 'Sienta':
        result = 292
    elif Model == 'Sigra':
        result = 293
    elif Model == 'Sirion':
        result = 294
    elif Model == 'Skyline':
        result = 295
    elif Model == 'Soluna':
        result = 296
    elif Model == 'Sonata':
        result = 297
    elif Model == 'Sorento':
        result = 298
    elif Model == 'Spark':
        result = 299
    elif Model == 'Spin':
        result = 300
    elif Model == 'Splash':
        result = 301
    elif Model == 'Sportage':
        result = 302
    elif Model == 'Starlet':
        result = 303
    elif Model == 'Strada':
        result = 304
    elif Model == 'Strada Triton':
        result = 305
    elif Model == 'Stream':
        result = 306
    elif Model == 'Succed':
        result = 307
    elif Model == 'Swift':
        result = 308
    elif Model == 'T120SS':
        result = 309
    elif Model == 'Taft':
        result = 310
    elif Model == 'Taruna':
        result = 311
    elif Model == 'Tavera':
        result = 312
    elif Model == 'Teana':
        result = 313
    elif Model == 'Telstar':
        result = 314
    elif Model == 'Terios':
        result = 315
    elif Model == 'Terrano':
        result = 316
    elif Model == 'Tiger':
        result = 317
    elif Model == 'Tiguan':
        result = 318
    elif Model == 'Touareg':
        result = 319
    elif Model == 'Touran':
        result = 320
    elif Model == 'Trailblazer':
        result = 321
    elif Model == 'Trajet':
        result = 322
    elif Model == 'Travello':
        result = 323
    elif Model == 'Trax':
        result = 324
    elif Model == 'Tribute':
        result = 325
    elif Model == 'Triton':
        result = 326
    elif Model == 'Trooper':
        result = 327
    elif Model == 'V-Class':
        result = 328
    elif Model == 'Vantrend':
        result = 329
    elif Model == 'Vellfire':
        result = 330
    elif Model == 'Verna':
        result = 331
    elif Model == 'Viano':
        result = 332
    elif Model == 'Vios':
        result = 333
    elif Model == 'Visto':
        result = 334
    elif Model == 'Voltz':
        result = 335
    elif Model == 'Voxy':
        result = 336
    elif Model == 'Wagon R':
        result = 337
    elif Model == 'Willys':
        result = 338
    elif Model == 'Winner':
        result = 339
    elif Model == 'Wira':
        result = 340
    elif Model == 'Wrangler':
        result = 341
    elif Model == 'X-Trail':
        result = 342
    elif Model == 'X1':
        result = 343
    elif Model == 'X3':
        result = 344
    elif Model == 'X4':
        result = 345
    elif Model == 'X5':
        result = 346
    elif Model == 'X6':
        result = 347
    elif Model == 'Xenia':
        result = 348
    elif Model == 'Xpander':
        result = 349
    elif Model == 'Yaris':
        result = 350
    elif Model == 'Z4':
        result = 351
    elif Model == 'Zafira':
        result = 352
    elif Model == 'Zebra':
        result = 353
    elif Model == 'i10':
        result = 354
    elif Model == 'i20':
        result = 355
    elif Model == 'i8':
        result = 356
    elif Model == 'ist':
        result = 357
    elif Model == 'laser':
        result = 358
    return result

def VAR(Varian):
      #result = None # Nilai default jika tidak ada kondisi yang terpenuhi
    if Varian == '1,4 L':
        result = 0
    elif Varian == '1.0':
        result = 1
    elif Varian == '1.0 D':
        result = 2
    elif Varian == '1.0 M':
        result = 3
    elif Varian == '1.1 L':
        result = 4
    elif Varian == '1.2':
        result = 5
    elif Varian == '1.2 NA':
        result = 6
    elif Varian == '1.2 R':
        result = 7
    elif Varian == '1.2 X':
        result = 8
    elif Varian == '1.2L':
        result = 9
    elif Varian == '1.2L XS':
        result = 10
    elif Varian == '1.3':
        result = 11
    elif Varian == '1.3 Sedan':
        result = 12
    elif Varian == '1.4':
        result = 13
    elif Varian == '1.4 TFSI':
        result = 14
    elif Varian == '1.4 TSI':
        result = 15
    elif Varian == '1.5':
        result = 16
    elif Varian == '1.5 CVT':
        result = 17
    elif Varian == '1.5 DOHC':
        result = 18
    elif Varian == '1.5 Exi':
        result = 19
    elif Varian == '1.5 Hybrid':
        result = 20
    elif Varian == '1.5L':
        result = 21
    elif Varian == '1.5L A':
        result = 22
    elif Varian == '1.5L S':
        result = 23
    elif Varian == '1.6':
        result = 24
    elif Varian == '1.6 GLXi':
        result = 25
    elif Varian == '1.6 L':
        result = 26
    elif Varian == '1.6 NA':
        result = 27
    elif Varian == '1.6 Sedan':
        result = 28
    elif Varian == '1.8':
        result = 29
    elif Varian == '1.8 GLXi':
        result = 30
    elif Varian == '1.8 NA':
        result = 31
    elif Varian == '1.8 SEi':
        result = 32
    elif Varian == '1.8 TFSI PI':
        result = 33
    elif Varian == '1.8L':
        result = 34
    elif Varian == '1.8L Prestige':
        result = 35
    elif Varian == '1.9':
        result = 36
    elif Varian == '10-S':
        result = 37
    elif Varian == '120i Steptronic':
        result = 38
    elif Varian == '13.3':
        result = 39
    elif Varian == '2,5 G':
        result = 40
    elif Varian == '2,5 V':
        result = 41
    elif Varian == '2.0':
        result = 42
    elif Varian == '2.0 16V':
        result = 43
    elif Varian == '2.0 Evolution 3':
        result = 44
    elif Varian == '2.0 Manual':
        result = 45
    elif Varian == '2.0 Prestige':
        result = 46
    elif Varian == '2.0 S TFSI':
        result = 47
    elif Varian == '2.0 SKYACTIV':
        result = 48
    elif Varian == '2.0 Sedan':
        result = 49
    elif Varian == '2.0 TFSI':
        result = 50
    elif Varian == '2.0 TFSI PI':
        result = 51
    elif Varian == '2.0 i-VTEC':
        result = 52
    elif Varian == '2.0L':
        result = 53
    elif Varian == '2.2':
        result = 54
    elif Varian == '2.3':
        result = 55
    elif Varian == '2.3 Ecoboost':
        result = 56
    elif Varian == '2.4':
        result = 57
    elif Varian == '2.4 NA':
        result = 58
    elif Varian == '2.4 Prestige':
        result = 59
    elif Varian == '2.4 Spirit S1':
        result = 60
    elif Varian == '2.4 i-VTEC':
        result = 61
    elif Varian == '2.4L Prestige':
        result = 62
    elif Varian == '2.4L Vti':
        result = 63
    elif Varian == '2.5':
        result = 64
    elif Varian == '2.5 Basic':
        result = 65
    elif Varian == '2.5 CRDi':
        result = 66
    elif Varian == '2.5 D Pickup':
        result = 67
    elif Varian == '2.5 Diesel':
        result = 68
    elif Varian == '2.5 Diesel Tdi':
        result = 69
    elif Varian == '2.5 G':
        result = 70
    elif Varian == '2.5 L':
        result = 71
    elif Varian == '2.5 L AT':
        result = 72
    elif Varian == '2.5 L AT Premiere':
        result = 73
    elif Varian == '2.5 Manual':
        result = 74
    elif Varian == '2.5 Middle':
        result = 75
    elif Varian == '2.5 NA':
        result = 76
    elif Varian == '2.5 TDi NA':
        result = 77
    elif Varian == '2.5 X':
        result = 78
    elif Varian == '2.5L Dakar':
        result = 79
    elif Varian == '2.5L Diesel NA':
        result = 80
    elif Varian == '2.8':
        result = 81
    elif Varian == '2.8 FSI S-Line':
        result = 82
    elif Varian == '2.8 Minibus Diesel':
        result = 83
    elif Varian == '2.9':
        result = 84
    elif Varian == '2000':
        result = 85
    elif Varian == '200T AL20':
        result = 86
    elif Varian == '200T F Sport':
        result = 87
    elif Varian == '200T F-Sport':
        result = 88
    elif Varian == '218i':
        result = 89
    elif Varian == '218i Sport Line Active Tour':
        result = 90
    elif Varian == '230 JS':
        result = 91
    elif Varian == '240G':
        result = 92
    elif Varian == '250 XV':
        result = 93
    elif Varian == '270':
        result = 94
    elif Varian == '270 AL10':
        result = 95
    elif Varian == '3.0 TFSI Quattro':
        result = 96
    elif Varian == '3.0 TFSI V6 Special Package':
        result = 97
    elif Varian == '3.2':
        result = 98
    elif Varian == '3.3':
        result = 99
    elif Varian == '3.5 Q':
        result = 100
    elif Varian == '3.7 NA':
        result = 101
    elif Varian == '3.9':
        result = 102
    elif Varian == '300':
        result = 103
    elif Varian == '300 Series':
        result = 104
    elif Varian == '300G':
        result = 105
    elif Varian == '300H':
        result = 106
    elif Varian == '318i':
        result = 107
    elif Varian == '318i 1.8':
        result = 108
    elif Varian == '318i 2.0':
        result = 109
    elif Varian == '318i E30 1.8':
        result = 110
    elif Varian == '318i E36 1.8':
        result = 111
    elif Varian == '318i E46 1.8':
        result = 112
    elif Varian == '318i E46 1.9':
        result = 113
    elif Varian == '318i E46 Fac  elift 2.0':
        result = 114    
    elif Varian == '320d':
        result = 115
    elif Varian == '320d Modern':
        result = 116
    elif Varian == '320i':
        result = 117
    elif Varian == '320i 2.0':
        result = 118
    elif Varian == '320i Business Edition':
        result = 119
    elif Varian == '320i E36 2.0':
        result = 120
    elif Varian == '320i E90 2.0':
        result = 121
    elif Varian == '320i E90 Fac  elift':
        result = 122    
    elif Varian == '320i E90 LCI':
        result = 123
    elif Varian == '320i Luxury':
        result = 124
    elif Varian == '320i M Sport':
        result = 125
    elif Varian == '320i Sport':
        result = 126
    elif Varian == '323i':
        result = 127
    elif Varian == '323i E36 2.5':
        result = 128
    elif Varian == '323i E46 2.5':
        result = 129
    elif Varian == '325Ci 2.5 Coupe':
        result = 130
    elif Varian == '325i':
        result = 131
    elif Varian == '325i 2.5':
        result = 132
    elif Varian == '325i E46 L6':
        result = 133
    elif Varian == '325i E90 L6':
        result = 134
    elif Varian == '328i 2.0 Luxury':
        result = 135
    elif Varian == '328i 2.0 Sport':
        result = 136
    elif Varian == '328i Luxury':
        result = 137
    elif Varian == '328i Sport':
        result = 138
    elif Varian == '330i':
        result = 139
    elif Varian == '330i 2.0 M Sport':
        result = 140
    elif Varian == '330i 3.0':
        result = 141
    elif Varian == '330i M Sport':
        result = 142
    elif Varian == '335i':
        result = 143
    elif Varian == '335i Luxury':
        result = 144
    elif Varian == '350':
        result = 145
    elif Varian == '350 AL10':
        result = 146
    elif Varian == '350 F Sport':
        result = 147
    elif Varian == '350 XU30':
        result = 148
    elif Varian == '4 AT':
        result = 149
    elif Varian == '4.2 VX':
        result = 150
    elif Varian == '4.5 V8 Diesel':
        result = 151
    elif Varian == '400':
        result = 152
    elif Varian == '407':
        result = 153
    elif Varian == '408':
        result = 154
    elif Varian == '428i Convertible Sport':
        result = 155
    elif Varian == '430i Convertible Sport':
        result = 156
    elif Varian == '435i':
        result = 157
    elif Varian == '440i Gran Coupe M Sport':
        result = 158
    elif Varian == '460 L V8':
        result = 159
    elif Varian == '460 L V8 4.6':
        result = 160
    elif Varian == '460L':
        result = 161
    elif Varian == '470':
        result = 162
    elif Varian == '470 V8 4.7 Automatic':
        result = 163
    elif Varian == '4X2':
        result = 164
    elif Varian == '4X4':
        result = 165
    elif Varian == '5 MT':
        result = 166
    elif Varian == '520 E39 2.0':
        result = 167
    elif Varian == '520d':
        result = 168
    elif Varian == '520d 2.0L Diesel':
        result = 169
    elif Varian == '520d F10 2.0 Diesel':
        result = 170
    elif Varian == '520d F10 Fac  elift 2.0 Diesel':
        result = 171    
    elif Varian == '520i':
        result = 172
    elif Varian == '520i 2.0':
        result = 173
    elif Varian == '520i E28':
        result = 174
    elif Varian == '520i E34 2.0':
        result = 175
    elif Varian == '520i E39 Fac  elift 2.2 L6':
        result = 176    
    elif Varian == '520i E60 2.2 l6':
        result = 177
    elif Varian == '520i F10 Fac  elift 2.0':
        result = 178    
    elif Varian == '520i Luxury':
        result = 179
    elif Varian == '520i Modern':
        result = 180
    elif Varian == '523i':
        result = 181
    elif Varian == '523i E39 2.5':
        result = 182
    elif Varian == '523i E39 2.5 L6':
        result = 183
    elif Varian == '523i E60 2.5 L6':
        result = 184
    elif Varian == '525i':
        result = 185
    elif Varian == '528i':
        result = 186
    elif Varian == '528i E39 2.8':
        result = 187
    elif Varian == '528i E39 2.8 L6':
        result = 188
    elif Varian == '528i F10 2.0':
        result = 189
    elif Varian == '528i F10 Fac  elift 2.0':
        result = 190    
    elif Varian == '528i Luxury':
        result = 191
    elif Varian == '530i':
        result = 192
    elif Varian == '530i E60 Fac  elift L6 3.0':
        result = 193    
    elif Varian == '535i':
        result = 194
    elif Varian == '535i Luxury GT':
        result = 195
    elif Varian == '570':
        result = 196
    elif Varian == '570 Sport':
        result = 197
    elif Varian == '570 V8 5.7 Automatic':
        result = 198
    elif Varian == '600':
        result = 199
    elif Varian == '630i 3.0':
        result = 200
    elif Varian == '630i E63 L6 3.0':
        result = 201
    elif Varian == '640i':
        result = 202
    elif Varian == '7.7':
        result = 203
    elif Varian == '730Li':
        result = 204
    elif Varian == '730Li Comfort':
        result = 205
    elif Varian == '730Li E65':
        result = 206
    elif Varian == '730i':
        result = 207
    elif Varian == '730i E38 V8 3.0':
        result = 208
    elif Varian == '735IL V8 3.5':
        result = 209
    elif Varian == '735Li':
        result = 210
    elif Varian == '740Li':
        result = 211
    elif Varian == '740Li F02':
        result = 212
    elif Varian == '750Li':
        result = 213
    elif Varian == 'A':
        result = 214
    elif Varian == 'A/T':
        result = 215
    elif Varian == 'A/T Option':
        result = 216
    elif Varian == 'A140':
        result = 217
    elif Varian == 'A150':
        result = 218
    elif Varian == 'A200':
        result = 219
    elif Varian == 'A250':
        result = 220
    elif Varian == 'A45':
        result = 221
    elif Varian == 'ACTIV':
        result = 222
    elif Varian == 'Absolute V6':
        result = 223
    elif Varian == 'Adventure R':
        result = 224
    elif Varian == 'Autech':
        result = 225
    elif Varian == 'Autobiography':
        result = 226
    elif Varian == 'Automatic':
        result = 227
    elif Varian == 'B170':
        result = 228
    elif Varian == 'B200':
        result = 229
    elif Varian == 'BLM':
        result = 230
    elif Varian == 'Base':
        result = 231
    elif Varian == 'Base Plus':
        result = 232
    elif Varian == 'Basic':
        result = 233
    elif Varian == 'Blind Van High':
        result = 234
    elif Varian == 'Box 3.3':
        result = 235
    elif Varian == 'Bus Chassis':
        result = 236
    elif Varian == 'Bus Chassis':
        result = 237
    elif Varian == 'Bus Diesel NA':
        result = 238
    elif Varian == 'C180':
        result = 239
    elif Varian == 'C200':
        result = 240
    elif Varian == 'C200K':
        result = 241
    elif Varian == 'C230':
        result = 242
    elif Varian == 'C240':
        result = 243
    elif Varian == 'C250':
        result = 244
    elif Varian == 'C280':
        result = 245
    elif Varian == 'C300':
        result = 246
    elif Varian == 'C320':
        result = 247
    elif Varian == 'CD':
        result = 248
    elif Varian == 'CFE Prime':
        result = 249
    elif Varian == 'CL':
        result = 250
    elif Varian == 'CLA200':
        result = 251
    elif Varian == 'CLA45 AMG':
        result = 252
    elif Varian == 'CLC200':
        result = 253
    elif Varian == 'CLS350':
        result = 254
    elif Varian == 'CLS400':
        result = 255
    elif Varian == 'CLS63 5.5 AMG':
        result = 256
    elif Varian == 'CLS63 AMG':
        result = 257
    elif Varian == 'CPS':
        result = 258
    elif Varian == 'CPS B-Line':
        result = 259
    elif Varian == 'CPS Executive':
        result = 260
    elif Varian == 'CPS FL':
        result = 261
    elif Varian == 'CPS Supreme':
        result = 262
    elif Varian == 'CRDi':
        result = 263
    elif Varian == 'CSR':
        result = 264
    elif Varian == 'CSX':
        result = 265
    elif Varian == 'CX':
        result = 266
    elif Varian == 'Coupe':
        result = 267
    elif Varian == 'Cross Over':
        result = 268
    elif Varian == 'Cross Road':
        result = 269
    elif Varian == 'Custom':
        result = 270
    elif Varian == 'D':
        result = 271
    elif Varian == 'D 1.0 Plus':
        result = 272
    elif Varian == 'D 1.0 STD':
        result = 273
    elif Varian == 'D Drift':
        result = 274
    elif Varian == 'D FMC':
        result = 275
    elif Varian == 'D FMC Deluxe':
        result = 276
    elif Varian == 'D Sport':
        result = 277
    elif Varian == 'DILAGO':
        result = 278
    elif Varian == 'DX':
        result = 279
    elif Varian == 'Dakar':
        result = 280
    elif Varian == 'Dakar 2.4':
        result = 281
    elif Varian == 'Deluxe':
        result = 282
    elif Varian == 'Diamond':
        result = 283
    elif Varian == 'Dreza':
        result = 284
    elif Varian == 'Dreza GS':
        result = 285
    elif Varian == 'Dspec':
        result = 286
    elif Varian == 'Dspec CRDi':
        result = 287
    elif Varian == 'Dynamic Luxury Si4':
        result = 288
    elif Varian == 'Dynamic Si4':
        result = 289
    elif Varian == 'E':
        result = 290
    elif Varian == 'E CVT':
        result = 291
    elif Varian == 'E Limited Edition':
        result = 292
    elif Varian == 'E Mugen':
        result = 293
    elif Varian == 'E Prestige':
        result = 294
    elif Varian == 'E STD':
        result = 295
    elif Varian == 'E Special Editon':
        result = 296
    elif Varian == 'E200':
        result = 297
    elif Varian == 'E200K':
        result = 298
    elif Varian == 'E220':
        result = 299
    elif Varian == 'E230':
        result = 300
    elif Varian == 'E240':
        result = 301
    elif Varian == 'E250':
        result = 302
    elif Varian == 'E260':
        result = 303
    elif Varian == 'E280':
        result = 304
    elif Varian == 'E300':
        result = 305
    elif Varian == 'E320':
        result = 306
    elif Varian == 'E400':
        result = 307
    elif Varian == 'E53':
        result = 308
    elif Varian == 'E53 Fac   elift 3.0 L6':
        result = 309    
    elif Varian == 'E63 AMG':
        result = 310
    elif Varian == 'E70 3.0 V6':
        result = 311
    elif Varian == 'E80':
        result = 312
    elif Varian == 'E89':
        result = 313
    elif Varian == 'ES Prestige':
        result = 314
    elif Varian == 'ES250':
        result = 315
    elif Varian == 'EX':
        result = 316
    elif Varian == 'EX AT':
        result = 317
    elif Varian == 'EX Sport AT':
        result = 318
    elif Varian == 'EXCEED A/T':
        result = 319
    elif Varian == 'EXCEED M/T':
        result = 320
    elif Varian == 'EcoBoost S':
        result = 321
    elif Varian == 'Elegance':
        result = 322
    elif Varian == 'Elegance Next Generion':
        result = 323
    elif Varian == 'Elite':
        result = 324
    elif Varian == 'Estilo':
        result = 325
    elif Varian == 'Exceed':
        result = 326
    elif Varian == 'Exceed Hi-Power':
        result = 327
    elif Varian == 'Extra X':
        result = 328
    elif Varian == 'F50 2.5L':
        result = 329
    elif Varian == 'F70 GT':
        result = 330
    elif Varian == 'F75 4X4 2.8':
        result = 331
    elif Varian == 'FD':
        result = 332
    elif Varian == 'FGX':
        result = 333
    elif Varian == 'FL':
        result = 334
    elif Varian == 'FLX':
        result = 335
    elif Varian == 'FSI':
        result = 336
    elif Varian == 'FX':
        result = 337
    elif Varian == 'Fac   elift':
        result = 338    
    elif Varian == 'G':
        result = 339
    elif Varian == 'G 1.8':
        result = 340
    elif Varian == 'G Basic':
        result = 341
    elif Varian == 'G Luxury':
        result = 342
    elif Varian == 'G S C Package':
        result = 343
    elif Varian == 'G TRD':
        result = 344
    elif Varian == 'G100':
        result = 345
    elif Varian == 'G300':
        result = 346
    elif Varian == 'GA':
        result = 347
    elif Varian == 'GE':
        result = 348
    elif Varian == 'GK':
        result = 349
    elif Varian == 'GL':
        result = 350
    elif Varian == 'GL Airbag':
        result = 351
    elif Varian == 'GL MT':
        result = 352
    elif Varian == 'GL Sporty':
        result = 353
    elif Varian == 'GL400':
        result = 354
    elif Varian == 'GL500':
        result = 355
    elif Varian == 'GL8':
        result = 356
    elif Varian == 'GLA200':
        result = 357
    elif Varian == 'GLA45 AMG':
        result = 358
    elif Varian == 'GLC250':
        result = 359
    elif Varian == 'GLE250':
        result = 360
    elif Varian == 'GLE250D':
        result = 361
    elif Varian == 'GLE400':
        result = 362
    elif Varian == 'GLE43 AMG':
        result = 363
    elif Varian == 'GLS':
        result = 364
    elif Varian == 'GLS M/T':
        result = 365
    elif Varian == 'GLS SE':
        result = 366
    elif Varian == 'GLS400':
        result = 367
    elif Varian == 'GLX':
        result = 368
    elif Varian == 'GLX M/T':
        result = 369
    elif Varian == 'GLXi':
        result = 370
    elif Varian == 'GS':
        result = 371
    elif Varian == 'GT':
        result = 372
    elif Varian == 'GT 2.0 TSI':
        result = 373
    elif Varian == 'GT2':
        result = 374
    elif Varian == 'GT3':
        result = 375
    elif Varian == 'GTI':
        result = 376
    elif Varian == 'GTS':
        result = 377
    elif Varian == 'GX':
        result = 378
    elif Varian == 'GX AT':
        result = 379
    elif Varian == 'GX Elegant':
        result = 380
    elif Varian == 'GX MT':
        result = 381
    elif Varian == 'Ghia':
        result = 382
    elif Varian == 'Gli':
        result = 383
    elif Varian == 'Grancoupe':
        result = 384
    elif Varian == 'Grand Touring':
        result = 385
    elif Varian == 'GrandRoad':
        result = 386
    elif Varian == 'Grandia':
        result = 387
    elif Varian == 'HD-X':
        result = 388
    elif Varian == 'HDI':
        result = 389
    elif Varian == 'HDX':
        result = 390
    elif Varian == 'HSE':
        result = 391
    elif Varian == 'HSE Si4':
        result = 392
    elif Varian == 'HWS':
        result = 393
    elif Varian == 'Hatchback':
        result = 394
    elif Varian == 'Heykers':
        result = 395
    elif Varian == 'Hi-Rider XLT':
        result = 396
    elif Varian == 'High':
        result = 397
    elif Varian == 'Hurricane':
        result = 398
    elif Varian == 'Hybrid':
        result = 399
    elif Varian == 'IS300 3.0':
        result = 400
    elif Varian == 'Interplay':
        result = 401
    elif Varian == 'J':
        result = 402
    elif Varian == 'JLX':
        result = 403
    elif Varian == 'JX':
        result = 404
    elif Varian == 'KL':
        result = 405
    elif Varian == 'KX':
        result = 406
    elif Varian == 'Kingsroad':
        result = 407
    elif Varian == 'Krista':
        result = 408
    elif Varian == 'L':
        result = 409
    elif Varian == 'L Hybrid':
        result = 410
    elif Varian == 'L4 1.4':
        result = 411
    elif Varian == 'L4 110SW 2.2':
        result = 412
    elif Varian == 'L4 2.0':
        result = 413
    elif Varian == 'LGX':
        result = 414
    elif Varian == 'LGX-D':
        result = 415
    elif Varian == 'LM':
        result = 416
    elif Varian == 'LS':
        result = 417
    elif Varian == 'LS Black Panther':
        result = 418
    elif Varian == 'LS Hi Grade':
        result = 419
    elif Varian == 'LSX':
        result = 420
    elif Varian == 'LSX-D':
        result = 421
    elif Varian == 'LT':
        result = 422
    elif Varian == 'LTD':
        result = 423
    elif Varian == 'LTZ':
        result = 424
    elif Varian == 'LV':
        result = 425
    elif Varian == 'LWB':
        result = 426
    elif Varian == 'LX':
        result = 427
    elif Varian == 'LX+':
        result = 428
    elif Varian == 'LX+ MT':
        result = 429
    elif Varian == 'Lain-lain':
        result = 430
    elif Varian == 'LeMans':
        result = 431
    elif Varian == 'Li':
        result = 432
    elif Varian == 'Li Deluxe':
        result = 433
    elif Varian == 'Li Family':
        result = 434
    elif Varian == 'Li Special Edition':
        result = 435
    elif Varian == 'Li Sporty':
        result = 436
    elif Varian == 'Limited':
        result = 437
    elif Varian == 'Limited Edition':
        result = 438
    elif Varian == 'Ltd':
        result = 439
    elif Varian == 'Luxury':
        result = 440
    elif Varian == 'Luxury Veloz':
        result = 441
    elif Varian == 'M':
        result = 442
    elif Varian == 'M 1.0 Deluxe':
        result = 443
    elif Varian == 'M 1.0 STD':
        result = 444
    elif Varian == 'M 1.0 Sporty':
        result = 445
    elif Varian == 'M Sport':
        result = 446
    elif Varian == 'M Sporty':
        result = 447
    elif Varian == 'M/T':
        result = 448
    elif Varian == 'M1 Coupe':
        result = 449
    elif Varian == 'M3':
        result = 450
    elif Varian == 'M4':
        result = 451
    elif Varian == 'ML250':
        result = 452
    elif Varian == 'ML320':
        result = 453
    elif Varian == 'ML400':
        result = 454
    elif Varian == 'Mega Carry':
        result = 455
    elif Varian == 'Mega Carry Box':
        result = 456
    elif Varian == 'Mi':
        result = 457
    elif Varian == 'Minibus 1.3':
        result = 458
    elif Varian == 'Minibus Standart':
        result = 459
    elif Varian == 'MkVII 1.2 TSI':
        result = 460
    elif Varian == 'MkVII 1.4 TSI':
        result = 461
    elif Varian == 'Option 2':
        result = 462
    elif Varian == 'Overland':
        result = 463
    elif Varian == 'PS 4.0':
        result = 464
    elif Varian == 'Panca A':
        result = 465
    elif Varian == 'Panca A Opt':
        result = 466
    elif Varian == 'Panca D':
        result = 467
    elif Varian == 'Panca T':
        result = 468
    elif Varian == 'Panca T Active':
        result = 469
    elif Varian == 'Panca T Opt':
        result = 470
    elif Varian == 'Panca T Style':
        result = 471
    elif Varian == 'Panca T Ultimate':
        result = 472
    elif Varian == 'Petrol':
        result = 473
    elif Varian == 'Pick Up':
        result = 474
    elif Varian == 'Pick Up 2.5':
        result = 475
    elif Varian == 'Pick Up Diesel':
        result = 476
    elif Varian == 'Pick Up Jumbo 1.3':
        result = 477
    elif Varian == 'Plantinum':
        result = 478
    elif Varian == 'Platinum':
        result = 479
    elif Varian == 'Prado 2.7':
        result = 480
    elif Varian == 'Prestige 2.4':
        result = 481
    elif Varian == 'Prestige Limited Edition':
        result = 482
    elif Varian == 'Q':
        result = 483
    elif Varian == 'R':
        result = 484
    elif Varian == 'R 1.3 Attivo':
        result = 485
    elif Varian == 'R 1.3 DLX':
        result = 486
    elif Varian == 'R 1.3 STD':
        result = 487
    elif Varian == 'R 1.3 Sporty':
        result = 488
    elif Varian == 'R280L':
        result = 489
    elif Varian == 'R300L':
        result = 490
    elif Varian == 'RAS':
        result = 491
    elif Varian == 'RC1':
        result = 492
    elif Varian == 'RCZ':
        result = 493
    elif Varian == 'RM':
        result = 494
    elif Varian == 'RS':
        result = 495
    elif Varian == 'RS 1.2':
        result = 496
    elif Varian == 'RS CVT':
        result = 497
    elif Varian == 'RS Limited Edition':
        result = 498
    elif Varian == 'RS M/T':
        result = 499
    elif Varian == 'RV. Gx':
        result = 500
    elif Varian == 'RX':
        result = 501
    elif Varian == 'RZ':
        result = 502
    elif Varian == 'Revolt':
        result = 503
    elif Varian == 'Rocky':
        result = 504
    elif Varian == 'Royale':
        result = 505
    elif Varian == 'Rubicon':
        result = 506
    elif Varian == 'Rubicon Unlimited':
        result = 507
    elif Varian == 'S':
        result = 508
    elif Varian == 'S 1.5':
        result = 509
    elif Varian == 'S 1.5C':
        result = 510
    elif Varian == 'S 1.5C LUX':
        result = 511
    elif Varian == 'S 1.5C LUX PLUS':
        result = 512
    elif Varian == 'S 1.5L':
        result = 513
    elif Varian == 'S 1.5L LUX':
        result = 514
    elif Varian == 'S CVT':
        result = 515
    elif Varian == 'S MT':
        result = 516
    elif Varian == 'S TDCi':
        result = 517
    elif Varian == 'S TRD Sportivo Luxury':
        result = 518
    elif Varian == 'S limited':
        result = 519
    elif Varian == 'S280':
        result = 520
    elif Varian == 'S3 Saloon':
        result = 521
    elif Varian == 'S300 L':
        result = 522
    elif Varian == 'S320':
        result = 523
    elif Varian == 'S350':
        result = 524
    elif Varian == 'S350 L':
        result = 525
    elif Varian == 'S400':
        result = 526
    elif Varian == 'S400 L':
        result = 527
    elif Varian == 'S500':
        result = 528
    elif Varian == 'S500 L':
        result = 529
    elif Varian == 'SE':
        result = 530
    elif Varian == 'SE 2':
        result = 531
    elif Varian == 'SE 3':
        result = 532
    elif Varian == 'SE Option':
        result = 533
    elif Varian == 'SE5':
        result = 534
    elif Varian == 'SEi':
        result = 535
    elif Varian == 'SG':
        result = 536
    elif Varian == 'SGX':
        result = 537
    elif Varian == 'SGX Arena':
        result = 538
    elif Varian == 'SGX Luxury':
        result = 539
    elif Varian == 'SL':
        result = 540
    elif Varian == 'SLK200':
        result = 541
    elif Varian == 'SLK200K':
        result = 542
    elif Varian == 'SLK230K':
        result = 543
    elif Varian == 'SLK250':
        result = 544
    elif Varian == 'SPORT':
        result = 545
    elif Varian == 'SPORT A/T':
        result = 546
    elif Varian == 'SRZ':
        result = 547
    elif Varian == 'ST':
        result = 548
    elif Varian == 'STD':
        result = 549
    elif Varian == 'SV':
        result = 550
    elif Varian == 'SW':
        result = 551
    elif Varian == 'SW HDI':
        result = 552
    elif Varian == 'SX':
        result = 553
    elif Varian == 'Sahara':
        result = 554
    elif Varian == 'Sahara CRD':
        result = 555
    elif Varian == 'Sahara Unlimited':
        result = 556
    elif Varian == 'Satya E':
        result = 557
    elif Varian == 'Satya S':
        result = 558
    elif Varian == 'Smart':
        result = 559
    elif Varian == 'Spacio 1.5':
        result = 560
    elif Varian == 'Spirit':
        result = 561
    elif Varian == 'Spirit R':
        result = 562
    elif Varian == 'Sport':
        result = 563
    elif Varian == 'Sport CRD Unlimited':
        result = 564
    elif Varian == 'Sport Renegrade':
        result = 565
    elif Varian == 'Sport Unlimited':
        result = 566
    elif Varian == 'Sport X':
        result = 567
    elif Varian == 'Sport+':
        result = 568
    elif Varian == 'Sportback':
        result = 569
    elif Varian == 'Sports Car':
        result = 570
    elif Varian == 'Sports E':
        result = 571
    elif Varian == 'Sports Version':
        result = 572
    elif Varian == 'Sporty':
        result = 573
    elif Varian == 'Sporty XS':
        result = 574
    elif Varian == 'Standard':
        result = 575
    elif Varian == 'Matic':
        result = 576
    elif Varian == 'Std':
        result = 577
    elif Varian == 'Strada':
        result = 578
    elif Varian == 'Style':
        result = 579
    elif Varian == 'Super Exceed':
        result = 580
    elif Varian == 'T':
        result = 581
    elif Varian == 'T2 2.6L':
        result = 582
    elif Varian == 'TD':
        result = 583
    elif Varian == 'TDI':
        result = 584
    elif Varian == 'TFSI':
        result = 585
    elif Varian == 'TFSI Quattro':
        result = 586
    elif Varian == 'TRD':
        result = 587
    elif Varian == 'TRD E Grade M/T':
        result = 588
    elif Varian == 'TRD G Luxury':
        result = 589
    elif Varian == 'TRD Sportivo':
        result = 590
    elif Varian == 'TRD Sportivo Heykers':
        result = 591
    elif Varian == 'TRD Sportivo TRD M/T':
        result = 592
    elif Varian == 'TRD Sportivo Ultimo':
        result = 593
    elif Varian == 'TS':
        result = 594
    elif Varian == 'TS Extra':
        result = 595
    elif Varian == 'TSI':
        result = 596
    elif Varian == 'TSI 1.2':
        result = 597
    elif Varian == 'TX':
        result = 598
    elif Varian == 'TX Adventure':
        result = 599
    elif Varian == 'Taft4X4':
        result = 600
    elif Varian == 'Td4':
        result = 601
    elif Varian == 'Titanium':
        result = 602
    elif Varian == 'Touring':
        result = 603
    elif Varian == 'Trailhawk':
        result = 604
    elif Varian == 'Trend':
        result = 605
    elif Varian == 'Truck':
        result = 606
    elif Varian == 'Turbo':
        result = 607
    elif Varian == 'Turbo 1.5':
        result = 608
    elif Varian == 'ULTIMATE A/T':
        result = 609
    elif Varian == 'Urban':
        result = 610
    elif Varian == 'V':
        result = 611
    elif Varian == 'V 1.8':
        result = 612
    elif Varian == 'V Diesel':
        result = 613
    elif Varian == 'V Luxury':
        result = 614
    elif Varian == 'V220':
        result = 615
    elif Varian == 'V6':
        result = 616
    elif Varian == 'V6 2.8':
        result = 617
    elif Varian == 'V6 3.0':
        result = 618
    elif Varian == 'V6 3.2':
        result = 619
    elif Varian == 'V6 3.6':
        result = 620
    elif Varian == 'V6 3.6':
        result = 621
    elif Varian == 'V6 4.0 Automatic':
        result = 622
    elif Varian == 'V6-24':
        result = 623
    elif Varian == 'V8 Supercharged':
        result = 624
    elif Varian == 'VL':
        result = 625
    elif Varian == 'VRZ':
        result = 626
    elif Varian == 'VTEC':
        result = 627
    elif Varian == 'VTi':
        result = 628
    elif Varian == 'VTi-L':
        result = 629
    elif Varian == 'VTi-S':
        result = 630
    elif Varian == 'VX Grade':
        result = 631
    elif Varian == 'Veloz':
        result = 632
    elif Varian == 'Venturer':
        result = 633
    elif Varian == 'Vti':
        result = 634
    elif Varian == 'WD':
        result = 635
    elif Varian == 'WildTrak':
        result = 636
    elif Varian == 'X':
        result = 637
    elif Varian == 'X 1.3 Plus':
        result = 638
    elif Varian == 'X 1.3 STD':
        result = 639
    elif Varian == 'X Deluxe':
        result = 640
    elif Varian == 'X Elegant':
        result = 641
    elif Varian == 'X Prestige':
        result = 642
    elif Varian == 'X-Gear':
        result = 643
    elif Varian == 'X4':
        result = 644
    elif Varian == 'XG Next Generion':
        result = 645
    elif Varian == 'XL':
        result = 646
    elif Varian == 'XLS':
        result = 647
    elif Varian == 'XLT':
        result = 648
    elif Varian == 'XLT-D':
        result = 649
    elif Varian == 'XR':
        result = 650
    elif Varian == 'XS':
        result = 651
    elif Varian == 'XV':
        result = 652
    elif Varian == 'XV10':
        result = 653
    elif Varian == 'Xi':
        result = 654
    elif Varian == 'Xi Deluxe':
        result = 655
    elif Varian == 'Xi Family':
        result = 656
    elif Varian == 'Xi Special Edition':
        result = 657
    elif Varian == 'Xi Sporty':
        result = 658
    elif Varian == 'Xli':
        result = 659
    elif Varian == 'Z':
        result = 660
    elif Varian == 'ZG':
        result = 661
    elif Varian == 'ZSX':
        result = 662
    elif Varian == 'i-DSI':
        result = 663
    elif Varian == 'sDrive 23i':
        result = 664
    elif Varian == 'sDrive18i':
        result = 665
    elif Varian == 'sDrive18i Business':
        result = 666
    elif Varian == 'sDrive18i Executive':
        result = 667
    elif Varian == 'sDrive18i xLine':
        result = 668
    elif Varian == 'sDrive20d':
        result = 669
    elif Varian == 'sDrive20d Sport Edition':
        result = 670
    elif Varian == 'sDrive20i':
        result = 671
    elif Varian == 'sDrive23i':
        result = 672
    elif Varian == 'sport-renegrade':
        result = 673
    elif Varian == 'xDrive20d Efficient Dynamics':
        result = 674
    elif Varian == 'xDrive20d xLine':
        result = 675
    elif Varian == 'xDrive20i xLine':
        result = 676
    elif Varian == 'xDrive25d':
        result = 677
    elif Varian == 'xDrive30d':
        result = 678
    elif Varian == 'xDrive35i':
        result = 679
    elif Varian == 'xDrive35i Executive':
        result = 680
    elif Varian == 'xDrive35i xLine':
        result = 681
    return result

def THN(Tahun):
    if Tahun == '1986':
        result = 0
    elif Tahun == '1987':
        result = 1
    elif Tahun == '1988':
        result = 2
    elif Tahun == '1989':
        result = 3
    elif Tahun == '1990':
        result = 4
    elif Tahun == '1991':
        result = 5
    elif Tahun == '1992':
        result = 6
    elif Tahun == '1993':
        result = 7
    elif Tahun == '1994':
        result = 8
    elif Tahun == '1995':
        result = 9
    elif Tahun == '1996':
        result = 10
    elif Tahun == '1997':
        result = 11
    elif Tahun == '1998':
        result = 12
    elif Tahun == '1999':
        result = 13
    elif Tahun == '2000':
        result = 14
    elif Tahun == '2001':
        result = 15
    elif Tahun == '2002':
        result = 16
    elif Tahun == '2003':
        result = 17
    elif Tahun == '2004':
        result = 18
    elif Tahun == '2005':
        result = 19
    elif Tahun == '2006':
        result = 20
    elif Tahun == '2007':
        result = 21
    elif Tahun == '2008':
        result = 22
    elif Tahun == '2009':
        result = 23
    elif Tahun == '2010':
        result = 24
    elif Tahun == '2011':
        result = 25
    elif Tahun == '2012':
        result = 26
    elif Tahun == '2013':
        result = 27
    elif Tahun == '2014':
        result = 28
    elif Tahun == '2015':
        result = 29
    elif Tahun == '2016':
        result = 30
    elif Tahun == '2017':
        result = 31
    elif Tahun == '2018':
        result = 32
    elif Tahun == '2019':
        result = 33
    elif Tahun == '<1986':
        result = 34
    return result

def JT(Jarak_tempuh):
    if Jarak_tempuh == '10.000':
        result = 0
    elif Jarak_tempuh == '100.000':
        result = 1
    elif Jarak_tempuh == '105.000':
        result = 2
    elif Jarak_tempuh == '110.000':
        result = 3
    elif Jarak_tempuh == '115.000':
        result = 4
    elif Jarak_tempuh == '120.000':
        result = 5
    elif Jarak_tempuh == '125.000':
        result = 6
    elif Jarak_tempuh == '130.000':
        result = 7
    elif Jarak_tempuh == '135.000':
        result = 8
    elif Jarak_tempuh == '140.000':
        result = 9
    elif Jarak_tempuh == '145.000':
        result = 10
    elif Jarak_tempuh == '15.000':
        result = 11
    elif Jarak_tempuh == '150.000':
        result = 12
    elif Jarak_tempuh == '155.000':
        result = 13
    elif Jarak_tempuh == '160.000':
        result = 14
    elif Jarak_tempuh == '165.000':
        result = 15
    elif Jarak_tempuh == '170.000':
        result = 16
    elif Jarak_tempuh == '175.000':
        result = 17
    elif Jarak_tempuh == '180.000':
        result = 18
    elif Jarak_tempuh == '185.000':
        result = 19
    elif Jarak_tempuh == '190.000':
        result = 20
    elif Jarak_tempuh == '195.000':
        result = 21
    elif Jarak_tempuh == '20.000':
        result = 22
    elif Jarak_tempuh == '200.000':
        result = 23
    elif Jarak_tempuh == '205.000':
        result = 24
    elif Jarak_tempuh == '210.000':
        result = 25
    elif Jarak_tempuh == '215.000':
        result = 26
    elif Jarak_tempuh == '220.000':
        result = 27
    elif Jarak_tempuh == '225.000':
        result = 28
    elif Jarak_tempuh == '230.000':
        result = 29
    elif Jarak_tempuh == '235.000':
        result = 30
    elif Jarak_tempuh == '240.000':
        result = 31
    elif Jarak_tempuh == '245.000':
        result = 32
    elif Jarak_tempuh == '25.000':
        result = 33
    elif Jarak_tempuh == '250.000':
        result = 34
    elif Jarak_tempuh == '255.000':
        result = 35
    elif Jarak_tempuh == '260.000':
        result = 36
    elif Jarak_tempuh == '265.000':
        result = 37
    elif Jarak_tempuh == '270.000':
        result = 38
    elif Jarak_tempuh == '275.000':
        result = 39
    elif Jarak_tempuh == '280.000':
        result = 40
    elif Jarak_tempuh == '285.000':
        result = 41
    elif Jarak_tempuh == '290.000':
        result = 42
    elif Jarak_tempuh == '295.000':
        result = 43
    elif Jarak_tempuh == '30.000':
        result = 44
    elif Jarak_tempuh == '300.000':
        result = 45
    elif Jarak_tempuh == '35.000':
        result = 46
    elif Jarak_tempuh == '40.000':
        result = 47
    elif Jarak_tempuh == '45.000':
        result = 48
    elif Jarak_tempuh == '5.000':
        result = 49
    elif Jarak_tempuh == '50.000':
        result = 50
    elif Jarak_tempuh == '55.000':
        result = 51
    elif Jarak_tempuh == '60.000':
        result = 52
    elif Jarak_tempuh == '65.000':
        result = 53
    elif Jarak_tempuh == '70.000':
        result = 54
    elif Jarak_tempuh == '75.000':
        result = 55
    elif Jarak_tempuh == '80.000':
        result = 56
    elif Jarak_tempuh == '85.000':
        result = 57
    elif Jarak_tempuh == '90.000':
        result = 58
    elif Jarak_tempuh == '95.000':
        result = 59
    return result
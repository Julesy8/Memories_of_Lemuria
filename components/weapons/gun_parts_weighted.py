import components.weapons.bullets as bullets

bullets_9mm_weighted = {
    bullets.round_9mm_115_fmj: (100, 90, 80, 75),
    bullets.round_9mm_124_fmj: (50,  55, 60, 65),
    bullets.round_9mm_147_fp:  (0,   10, 20, 25),
    bullets.round_9mm_115_jhp: (30,  35, 40, 45),
    bullets.round_9mm_124_jhp: (20,  25, 30, 35),
    bullets.round_9mm_147_jhp: (0,   5,  10, 15),

    bullets.round_9mm_115_fmj_pp: (0, 0, 20, 25),
    bullets.round_9mm_124_fmj_pp: (0, 0, 15, 20),
    bullets.round_9mm_147_fp_pp:  (0, 0, 7,  12),
    bullets.round_9mm_115_jhp_pp: (0, 0, 15, 20),
    bullets.round_9mm_124_jhp_pp: (0, 0, 7,  12),
    bullets.round_9mm_147_jhp_pp: (0, 0, 4,  9),
}

bullets_10mm_weighted = {
    bullets.round_10mm_155_jhp: (10, 10, 5, 5),
    bullets.round_10mm_180_fmj: (5,  6, 5,  5),
    bullets.round_10mm_190_jhp: (1,  2, 1,  2),
    bullets.round_10mm_220_fp:  (1,  2, 1,  2),
}

bullets_40sw_weighted = {
    bullets.round_40sw_155_jhp: (10, 10, 5),
    bullets.round_40sw_165_fmj: (5,  6,  5),
    bullets.round_40sw_180_fmj: (1,  2,  2),
    bullets.round_40sw_180_jhp: (0,  1,  2),
    bullets.round_40sw_220_fp:  (0,  1,  1),
}

bullets_10mm_40sw_weighted = {
    bullets.round_10mm_155_jhp: (10, 10, 5, 5),
    bullets.round_10mm_180_fmj: (5, 6, 5, 5),
    bullets.round_10mm_190_jhp: (1, 2, 1, 2),
    bullets.round_10mm_220_fp: (1, 2, 1, 2),
    bullets.round_40sw_155_jhp: (10, 10, 5),
    bullets.round_40sw_165_fmj: (5, 6, 5),
    bullets.round_40sw_180_fmj: (1, 2, 2),
    bullets.round_40sw_180_jhp: (0, 1, 2),
    bullets.round_40sw_220_fp: (0, 1, 1),
}

bullets_76225_weighted = {
    bullets.round_76225_85_rn:   (5, 5, 5),
    bullets.round_76225_90_jhp:  (1, 2, 3),
    bullets.round_76225_100_jhp: (0, 1, 2),
}

bullets_45_weighted = {
    bullets.round_45_185_swc: (100, 90, 80, 75),
    bullets.round_45_200_swc: (50,  55, 60, 65),
    bullets.round_45_185_jhp: (30,  35, 40, 45),
    bullets.round_45_200_jhp: (20,  25, 30, 35),
    bullets.round_45_230_jhp: (0,   5,  10, 15),
    bullets.round_45_200_fmj: (25,  30, 35, 40),
    bullets.round_45_230_fmj: (0,   10, 20, 25),

    bullets.round_45_185_swc_pp: (0, 0, 20, 25),
    bullets.round_45_200_swc_pp: (0, 0, 15, 20),
    bullets.round_45_185_jhp_pp: (0, 0, 15, 20),
    bullets.round_45_230_jhp_pp: (0, 0, 5, 10),
    bullets.round_45_200_fmj_pp: (0, 0, 15, 20),
    bullets.round_45_230_fmj_pp: (0, 0, 7, 12),
}

bullets_752_weighted = {
    bullets.round_76239_123_fmj: (5,  10, 10, 10),
    bullets.round_76239_150_fmj: (1,  3,  5,  5),
    bullets.round_76239_123_sst: (0,  1,  3,  4),
    bullets.round_76239_150_sp:  (0,  0,  1,  3),
}

bullets_556_weighted = {
    bullets.round_556_55_sp:  (10, 10, 5, 0, 0),
    bullets.round_556_60_fmj: (5,  5,  5, 0, 0),
    bullets.round_556_75_fmj: (1,  3,  3, 5, 5),
    bullets.round_556_69_jhp: (0,  1,  2, 5, 5),
    bullets.round_556_80_jhp: (0,  0,  1, 1, 3),
}

bullets_300aac_weighted = {
    bullets.round_300aac_150_jhp: (0, 1, 2),
    bullets.round_300aac_150_fmj: (5, 5, 3),
    bullets.round_300aac_210_fmj: (1, 2, 2),
    bullets.round_300aac_210_jhp: (0, 0, 1),
}

bullets_545_weighted = {
    bullets.round_545_56_fmj: (10, 10, 5, 0, 0),
    bullets.round_545_63_fmj: (1,  3,  3, 5, 5),
    bullets.round_545_60_jhp: (1,  2,  2, 3, 4),
}

bullets_308_weighted = {
    bullets.round_308_130_jhp: (10, 10, 5, 0, 0),
    bullets.round_308_150_fmj: (1, 3, 3, 5, 5),
    bullets.round_308_165_sp: (0, 1, 2, 3, 5),
    bullets.round_308_180_tsx: (0, 0, 1, 1, 3),
}

bullets_54r_weighted = {
    # bullets.round_54r_174_jrn: (10, 10, 5, 0, 0),
    bullets.round_54r_180_jsp: (1,  3,  3, 5, 5),
    bullets.round_54r_200_fmj: (1,  2,  2, 3, 4),
}

bullets_12ga_weighted = {
    bullets.round_12ga_00buck: (1, 1, 10, 5),
    bullets.round_12ga_slug: (0, 0, 1, 1)
}

bullets_50gi_weighted = {
    bullets.round_50gi_330_rn: (10, 10, 5, 5, 5),
    bullets.round_50gi_255_swc: (1,  3,  3, 5, 5),
    bullets.round_50gi_275_jhp: (1,  2,  2, 3, 4),
}

bullets_44mag_weighted = {
    bullets.round_44_180_jhp: (10, 10, 5, 0, 0),
    bullets.round_44_200_jhp: (5, 5, 5, 0, 0),
    bullets.round_44_225_jhp: (1, 3, 3, 5, 5),
    bullets.round_44_240_sp: (0, 1, 2, 5, 5),
    bullets.round_44_300_sp: (0, 0, 1, 1, 3)
}
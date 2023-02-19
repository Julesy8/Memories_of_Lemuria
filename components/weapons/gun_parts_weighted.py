import components.weapons.ar15 as ar
import components.weapons.bullets as bullets
import components.weapons.attachments as attachments
import components.weapons.glock17 as glock17
import components.weapons.kalashnikov as ak
import components.weapons.mosin as mosin
import components.weapons.mac10 as mac10
import components.weapons.sks as sks

ar_parts_weighted = {
    ar.lower_ar15: 100,
    ar.lower_ar10: 50,
    ar.upper_ar_m16a2: 50,
    ar.upper_ar_m16a4: 50,
    ar.upper_ar10: 25,

    ar.ar_barrel_standard_556: 35,
    ar.ar_barrel_standard_556_midlen: 35,
    ar.ar_barrel_carbine_556: 25,
    ar.ar_barrel_carbine_556_carblen: 25,
    ar.ar_barrel_pistol_556: 20,
    ar.ar_barrel_pistol_556_pistollen: 20,
    ar.ar_barrel_carbine_300: 10,
    ar.ar_barrel_carbine_300_carbinelen: 10,
    ar.ar_barrel_pistol_300: 5,
    ar.ar_barrel_pistol_300_pistollen: 5,
    ar.ar_barrel_standard_308: 10,
    ar.ar_barrel_standard_308_midlen: 20,
    ar.ar_barrel_carbine_308_midlen: 15,
    ar.ar_barrel_carbine_308_carblen: 15,
    ar.ar_barrel_pistol_308_carblen: 5,
    ar.ar_barrel_pistol_308_pistollen: 5,

    ar.ar_stock_m16a2: 70,
    ar.ar_stock_moe: 50,
    ar.ar_stock_ubr: 40,
    ar.ar_stock_danieldefense: 45,
    ar.ar_stock_prs: 30,
    ar.ar_stock_maxim_cqb: 20,

    ar.ar_handguard_m16a1: 5,
    ar.ar_handguard_m16a2: 24,
    ar.ar_handguard_m16a2_carbine: 20,
    ar.ar_handguard_magpul: 14,
    ar.ar_handguard_magpul_carbine: 10,
    ar.ar_handguard_aero: 12,
    ar.ar_handguard_aero_carbine: 12,
    ar.ar_handguard_aero_pistol: 8,
    ar.ar_handguard_faxon: 12,
    ar.ar_handguard_faxon_carbine: 12,
    ar.ar_handguard_faxon_pistol: 8,
    ar.ar_handguard_mk18: 12,
    ar.ar10_handguard_a2: 20,
    ar.ar10_handguard_a2_carbine: 16,
    ar.ar10_handguard_wilson: 12,
    ar.ar_handguard_wilson_carbine: 12,
    ar.ar10_handguard_vseven: 10,
    ar.ar_handguard_vseven_carbine: 8,
    ar.ar_handguard_vseven_pistol: 5,
    ar.ar_handguard_hera_carbine: 8,
    ar.ar_handguard_atlas_carbine: 8,
    ar.ar_handguard_atlas_pistol: 5,

    ar.ar_grip_trybe: 35,
    ar.ar_grip_moe: 60,
    ar.ar_grip_hogue: 20,
    ar.ar_grip_strikeforce: 25,
    ar.ar_grip_a2: 80,
    ar.ar_grip_stark: 30,

    ar.ar15_buffer: 110,
    ar.ar15_buffer_heavy: 44,
    ar.ar15_buffer_light: 44,
    ar.ar10_buffer: 30,
    ar.ar10_buffer_heavy: 20,
    ar.ar10_buffer_light: 20,

    ar.ar15_muzzle_flashhider: 26,
    ar.ar15_muzzle_st6012: 16,
    ar.ar15_muzzle_mi_mb4: 20,
    ar.ar15_muzzle_cobra: 10,
    ar.ar15_300_muzzle_flashhider: 20,
    ar.ar15_300_muzzle_cobra: 10,
    ar.ar15_300_muzzle_pegasus: 8,
    ar.ar15_300_muzzle_strike: 15,

    ar.ar_front_sight: 260,
    ar.ar_carry_handle: 20,
    ar.carry_handle_optic_mount: 10,
}

attachments_weighted = {
    attachments.holosun503: 30,
    attachments.acog_ta01: 10,
    attachments.eotech_exps3: 20,
    attachments.aimpoint_comp: 20,
    attachments.kobra_ekp: 10,
    attachments.kobra_ekp_picrail: 10,
    attachments.amguh1: 15,
    attachments.compactprism: 20,
    attachments.pm2scope: 8,
    attachments.pso1: 15,
    attachments.okp7: 20,

    attachments.irons_sig_rear: 10,
    attachments.irons_sig_front: 10,
    attachments.irons_magpul_rear: 10,
    attachments.irons_magpul_front: 10,
    attachments.irons_dd_rear: 10,
    attachments.irons_dd_front: 10,
    attachments.irons_troy_rear: 10,
    attachments.irons_troy_front: 10,

    attachments.grip_hera_cqr: 6,
    attachments.grip_promag_vertical: 20,
    attachments.grip_jem_vertical: 20,
    attachments.grip_magpul_angled: 12,
    attachments.grip_magpul_mvg: 16,
    attachments.grip_aimtac_short: 15,
    attachments.grip_magpul_handstop: 12,
    attachments.grip_hipoint_folding: 5,

    attachments.suppressor_obsidian_45: 10,
    attachments.suppressor_wolfman_9mm: 10,
    attachments.suppressor_obsidian_9: 10,
    attachments.suppressor_saker_762: 10,

    attachments.adapter_mlok_picrail: 50,
    attachments.adapter_mlok_picrail_short: 50,
}

bullets_9mm_weighted = {
    bullets.round_9mm_115_fmj: 70,
    bullets.round_9mm_124_fmj: 50,
    bullets.round_9mm_147_fp: 20,
    bullets.round_9mm_115_jhp: 80,
    bullets.round_9mm_124_jhp: 50,
    bullets.round_9mm_147_jhp: 20,
    bullets.round_9mm_115_fmj_pp: 50,
    bullets.round_9mm_124_fmj_pp: 40,
    bullets.round_9mm_147_fp_pp: 30,
    bullets.round_9mm_115_jhp_pp: 50,
    bullets.round_9mm_124_jhp_pp: 40,
    bullets.round_9mm_147_jhp_pp: 20,
}

bullets_45_weighted = {
    bullets.round_45_185_swc: 80,
    bullets.round_45_200_swc: 50,
    bullets.round_45_185_jhp: 60,
    bullets.round_45_200_jhp: 40,
    bullets.round_45_230_jhp: 30,
    bullets.round_45_200_fmj: 50,
    bullets.round_45_230_fmj: 30,

    bullets.round_45_185_swc_pp: 60,
    bullets.round_45_200_swc_pp: 30,
    bullets.round_45_185_jhp_pp: 40,
    bullets.round_45_230_jhp_pp: 10,
    bullets.round_45_200_fmj_pp: 30,
    bullets.round_45_230_fmj_pp: 10,
}

bullets_752_weighted = {
    bullets.round_76239_123_fmj: 175,
    bullets.round_76239_150_fmj: 100,
    bullets.round_76239_123_sst: 175,
    bullets.round_76239_150_sp: 50,
}

bullets_556_weighted = {
    bullets.round_556_55_sp: 200,
    bullets.round_556_60_fmj: 100,
    bullets.round_556_75_fmj: 60,
    bullets.round_556_69_jhp: 90,
    bullets.round_556_80_jhp: 50,
}

bullets_300aac_weighted = {
    bullets.round_300aac_150_jhp: 125,
    bullets.round_300aac_150_fmj: 125,
    bullets.round_300aac_210_fmj: 50,
    bullets.round_300aac_210_jhp: 50,
}

bullets_545_weighted = {
    bullets.round_545_56_fmj: 190,
    bullets.round_545_63_fmj: 60,
    bullets.round_545_60_jhp: 50,
}

bullets_308_weighted = {
    bullets.round_308_130_jhp: 200,
    bullets.round_308_150_fmj: 125,
    bullets.round_308_165_sp: 100,
    bullets.round_308_180_tsx: 50,
}

bullets_54r_weighted = {
    bullets.round_54r_174_jrn: 250,
    bullets.round_54r_180_jsp: 170,
    bullets.round_54r_200_fmj: 80,
}

glock17_parts_weighted = {
    glock17.glock17_frame: 250,

    glock17.glock17_barrel: 90,
    glock17.glock17l_barrel: 60,
    glock17.glock_9in_barrel: 30,
    glock17.glock17_barrel_ported: 40,
    glock17.glock17l_barrel_ported: 30,

    glock17.glock17_slide: 80,
    glock17.glock17l_slide: 40,
    glock17.glock17_slide_optic: 60,
    glock17.glock17l_slide_optic: 30,
    glock17.glock17_slide_custom: 20,
    glock17.glock17l_slide_custom: 15,

    glock17.glock_switch: 20,
    glock17.glock_9mm_compensator: 20,
    glock17.glock_stock: 10,
    glock17.glock_pic_rail: 20,
    glock17.glock_pistol_brace: 15,
    glock17.suppressor_surefire_9mm: 10,
}

ak_parts_weighted = {
    ak.reciever_akm: 150,
    ak.reciever_ak74: 100,
    ak.reciever_100556: 50,

    ak.handguard_akm: 70,
    ak.handguard_amd65: 30,
    ak.handguard_ak74: 50,
    ak.handguard_romanian: 40,
    ak.handguard_ak100: 30,
    ak.handguard_B10M: 10,
    ak.handguard_leader: 10,
    ak.handguard_magpul: 30,

    ak.stock_akm: 20,
    ak.stock_rpk: 5,
    ak.stock_ak74: 15,
    ak.stock_ak100: 10,
    ak.stock_ak_underfolder: 15,
    ak.stock_ak_triangle: 10,
    ak.stock_ak12: 5,
    ak.stock_amd65: 10,
    ak.stock_pt1: 10,
    ak.stock_moe: 10,
    ak.stock_zhukov: 3,

    ak.barrel_ak762: 60,
    ak.barrel_ak545: 30,
    ak.barrel_ak556: 20,
    ak.barrel_rpk762: 30,
    ak.barrel_rpk545: 20,
    ak.barrel_ak762_short: 40,
    ak.barrel_ak545_short: 30,
    ak.barrel_ak556_short: 20,

    ak.grip_akm: 60,
    ak.grip_ak12: 10,
    ak.grip_sniper: 15,
    ak.grip_moe: 50,
    ak.grip_rk3: 30,
    ak.grip_tapco: 30,
    ak.grip_skeletonised: 20,
    ak.grip_hogue: 20,
    ak.grip_fab: 25,

    ak.muzzle_ak74: 20,
    ak.muzzle_dtk: 13,
    ak.muzzle_amd65: 10,
    ak.muzzle_akm: 30,
    ak.muzzle_akml: 15,
    ak.muzzle_lantac: 15,
    ak.muzzle_pbs4: 8,
    ak.muzzle_pbs1: 8,
    ak.muzzle_dynacomp: 10,

    ak.accessory_dustcoverrail: 15,
    ak.accessory_railsidemount: 20,
    ak.ak_ar_mag_adapter: 10,
}

m10_part_dict = {
    mac10.mac1045_lower: 150,
    mac10.mac109_lower: 150,

    mac10.mac1045_upper: 42,
    mac10.mac1045_upper_tactical: 16,
    mac10.mac1045_upper_max: 10,
    mac10.mac109_upper: 42,
    mac10.mac109_upper_tactical: 16,
    mac10.mac109_upper_max: 10,
    mac10.mac109_calico_conv: 5,
    mac10.mac109_upper_max31: 3,
    mac10.mac109_upper_max31k: 3,

    mac10.mac1045_barrel: 30,
    mac10.mac1045_max_barrel: 20,
    mac10.mac1045_carbine_barrel: 10,
    mac10.mac109_barrel: 30,
    mac10.mac109_max_barrel: 20,
    mac10.mac109_carbine_barrel: 10,
    mac10.max1031_barrel_1228: 7,
    mac10.max1031k_barrel_1228: 7,
    mac10.max1031_barrel_3410: 7,
    mac10.max1031k_barrel_3410: 7,

    mac10.mac1045_full_stock: 30,
    mac10.mac1045_folding_stock: 20,
    mac10.mac1045_stock: 100,

    mac10.mac10_carbine_handguard_m16a2: 20,
    mac10.mac10_carbine_handguard_picatinny: 20,
    mac10.mac109_carbine_handguard_m16a2: 20,
    mac10.mac109_carbine_handguard_picatinny: 20,
    mac10.mac10_vertical_grip: 15,
    mac10.mac10_optics_mount: 25,
    mac10.mac10_trirail: 20,
    mac10.mac10_ar_stock_adapter: 10,

    mac10.mac1045_sionics_suppressor: 10,
    mac10.mac109_sionics_suppressor: 10,
    mac10.mac1045_extended_barrel: 40,
    mac10.mac109_extended_barrel: 40,
}

mosin_part_dict = {
    mosin.mosin_stock: 70,
    mosin.mosin_stock_montecarlo: 20,
    mosin.mosin_archangel_stock: 10,
    mosin.mosin_carbine_stock: 40,
    mosin.mosin_obrez_stock: 30,

    mosin.mosin_barrel: 120,
    mosin.mosin_carbine_barrel: 80,
    mosin.mosin_obrez_barrel: 50,

    mosin.mosin_pic_scope_mount: 20,
    mosin.mosin_suppressor: 15,
    mosin.mosin_muzzlebreak: 20,
}

sks_part_dict = {
    sks.stock_sks: 20,
    sks.stock_sks_tapco: 20,
    sks.stock_sks_dragunov: 20,
    sks.stock_sks_fab: 20,
    sks.stock_sks_sabertooth: 20,
    sks.stock_sks_bullpup: 20,

    sks.barrel_sks: 60,
    sks.barrel_sks_shortened: 40,
    sks.barrel_sks_auto: 30,
    sks.barrel_sks_shortened_auto: 20,
    sks.barrel_sks_akmag: 60,
    sks.barrel_sks_shortened_akmag: 40,
    sks.barrel_sks_auto_akmag: 30,
    sks.barrel_sks_shortened_auto_akmag: 20,

    sks.sks_optics_mount: 20,
}

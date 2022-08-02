OUTPUTS = dict(
    # Anatomicals
    native_T1w=dict(
        suffix="T1w",
        space=None,
        datatype="anat",
        desc="preproc",
    ),
    native_brain_mask=dict(
        suffix="mask",
        space=None,
        datatype="anat",
        desc="brain",
    ),
    native_parcellation=dict(
        suffix="dseg",
        space=None,
        datatype="anat",
    ),
    native_csf=dict(
        suffix="probseg",
        space=None,
        datatype="anat",
        label="csf",
    ),
    native_wm=dict(
        suffix="probseg",
        space=None,
        datatype="anat",
        label="wm",
    ),
    native_gm=dict(
        suffix="probseg",
        space=None,
        datatype="anat",
        label="gm",
    ),
    native_T1w=dict(
        suffix="T1w",
        space=["MNI152NLin2009cAsym"],
        datatype="anat",
        desc="preproc",
    ),
    # "standard_T1w": [
    #     "anat",
    #     "space-MNI152NLin2009cAsym_desc-preproc_T1w.nii.gz",
    # ],
    # "standard_brain_mask": [
    #     "anat",
    #     "space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz",
    # ],
    # "standard_parcellation": [
    #     "anat",
    #     "space-MNI152NLin2009cAsym_dseg.nii.gz",
    # ],
    # "standard_csf": [
    #     "anat",
    #     "space-MNI152NLin2009cAsym_label-CSF_probseg.nii.gz",
    # ],
    # "standard_gm": [
    #     "anat",
    #     "space-MNI152NLin2009cAsym_label-GM_probseg.nii.gz",
    # ],
    # "standard_wm": [
    #     "anat",
    #     "space-MNI152NLin2009cAsym_label-WM_probseg.nii.gz",
    # ],
    # "native_to_mni_transform": [
    #     "anat",
    #     "from-T1w_to-MNI152NLin2009cAsym_mode-image_xfm.h5",
    # ],
    # "mni_to_native_transform": [
    #     "anat",
    #     "from-MNI152NLin2009cAsym_to-T1w_mode-image_xfm.h5",
    # ],
    # "native_to_fsnative_transform": [
    #     "anat",
    #     "from-T1w_to-fsnative_mode-image_xfm.txt",
    # ],
    # "fsnative_to_native_transform": [
    #     "anat",
    #     "from-fsnative_to-T1w_mode-image_xfm.txt",
    # ],
    # "smoothwm": ["anat", "hemi-*_smoothwm.surf.gii"],
    # "pial": ["anat", "hemi-*_pial.surf.gii"],
    # "midthickness": ["anat", "hemi-*_midthickness.surf.gii"],
    # "inflated": ["anat", "hemi-*_inflated.surf.gii"],
    # # DWI
    # "coreg_dwi_image": [
    #     "dwi",
    #     "space-T1w_desc-preproc_dwi.nii.gz",
    # ],
    # "coreg_dwi_bvec": [
    #     "dwi",
    #     "space-T1w_desc-preproc_dwi.bvec",
    # ],
    # "coreg_dwi_bval": [
    #     "dwi",
    #     "space-T1w_desc-preproc_dwi.bval",
    # ],
    # "coreg_dwi_grad": [
    #     "dwi",
    #     "space-T1w_desc-preproc_dwi.b",
    # ],
    # "coreg_dwiref_image": [
    #     "dwi",
    #     "space-T1w_dwiref.nii.gz",
    # ],
    # "coreg_dwi_brain_mask": [
    #     "dwi",
    #     "space-T1w_desc-brain_mask.nii.gz",
    # ],
)

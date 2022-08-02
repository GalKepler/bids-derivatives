from bids_derivatives.bids_apps.outputs.templates import STANDARD_SPACES

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
    standard_T1w=dict(
        suffix="T1w",
        space=STANDARD_SPACES,
        datatype="anat",
        desc="preproc",
    ),
    standard_brain_mask=dict(
        suffix="mask",
        space=STANDARD_SPACES,
        datatype="anat",
        desc="brain",
    ),
    standard_parcellation=dict(
        suffix="dseg",
        space=STANDARD_SPACES,
        datatype="anat",
        desc="brain",
    ),
    standard_csf=dict(
        suffix="probseg",
        space=STANDARD_SPACES,
        datatype="anat",
        label="csf",
    ),
    standard_wm=dict(
        suffix="probseg",
        space=STANDARD_SPACES,
        datatype="anat",
        label="wm",
    ),
    standard_gm=dict(
        suffix="probseg",
        space=STANDARD_SPACES,
        datatype="anat",
        label="gm",
    ),
    native_to_mni_transform={
        "suffix": "xfm",
        "from": "T1w",
        "to": STANDARD_SPACES,
        "mode": "image",
        "datatype": "anat",
        "extension": ".h5",
    },
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

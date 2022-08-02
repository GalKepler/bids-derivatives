from bids_derivatives.bids_apps.outputs.templates import STANDARD_SPACES

OUTPUTS = dict(
    # Anatomicals
    native_T1w={
        "entities": dict(
            suffix="T1w",
            space=None,
            datatype="anat",
            desc="preproc",
        ),
        "description": "Preprocessed anatomical image in native space.",
    },
    native_brain_mask={
        "entities": dict(
            suffix="mask",
            space=None,
            datatype="anat",
            desc="brain",
        ),
        "description": "Preprocessed anatomical brain mask in native space.",
    },
    native_parcellation={
        "entities": dict(
            suffix="dseg",
            space=None,
            datatype="anat",
        ),
        "description": "Preprocessed anatomical brain parcellation in native space.",  # noqa: E501
    },
    native_csf={
        "entities": dict(
            suffix="probseg",
            space=None,
            datatype="anat",
            label="csf",
        ),
        "description": "CSF probabilistic mask in native space.",
    },
    native_wm={
        "entities": dict(
            suffix="probseg",
            space=None,
            datatype="anat",
            label="wm",
        ),
        "description": "WM probabilistic mask in native space.",
    },
    native_gm={
        "entities": dict(
            suffix="probseg",
            space=None,
            datatype="anat",
            label="gm",
        ),
        "description": "GM probabilistic mask in native space.",
    },
    standard_T1w={
        "entities": dict(
            suffix="T1w",
            space=STANDARD_SPACES,
            datatype="anat",
            desc="preproc",
        ),
        "description": "Preprocessed anatomical image in standard space(s).",
    },
    standard_brain_mask={
        "entities": dict(
            suffix="mask",
            space=STANDARD_SPACES,
            datatype="anat",
            desc="brain",
        ),
        "description": "Preprocessed anatomical brain mask in standard space(s).",  # noqa: E501
    },
    standard_parcellation={
        "entities": dict(
            suffix="dseg",
            space=STANDARD_SPACES,
            datatype="anat",
            desc="brain",
        ),
        "description": "Preprocessed anatomical brain parcellation in standard space(s).",  # noqa: E501
    },
    standard_csf={
        "entities": dict(
            suffix="probseg",
            space=STANDARD_SPACES,
            datatype="anat",
            label="csf",
        ),
        "description": "CSF probabilistic mask in standard space(s).",
    },
    standard_wm={
        "entities": dict(
            suffix="probseg",
            space=STANDARD_SPACES,
            datatype="anat",
            label="wm",
        ),
        "description": "WM probabilistic mask in standard space(s).",
    },
    standard_gm={
        "entities": dict(
            suffix="probseg",
            space=STANDARD_SPACES,
            datatype="anat",
            label="gm",
        ),
        "description": "GM probabilistic mask in standard space(s).",
    },
    native_to_standard_transform={
        "entities": {
            "suffix": "xfm",
            "from": "T1w",
            "to": STANDARD_SPACES,
            "mode": "image",
            "datatype": "anat",
            "extension": ".h5",
        },
        "description": "Transformation file from native to standard space.",
    },
    standard_to_native_transform={
        "entities": {
            "suffix": "xfm",
            "from": STANDARD_SPACES,
            "to": "T1w",
            "mode": "image",
            "datatype": "anat",
            "extension": ".h5",
        },
        "description": "Transformation file from standard to native space.",
    },
    smoothwm={
        "entities": dict(
            suffix="smoothwm",
            datatype="anat",
            extension=".surf.gii",
            hemi=["L", "R"],
        ),
        "description": "Smoothed original surface meshes.",
    },
    pial={
        "entities": dict(
            suffix="pial",
            datatype="anat",
            extension=".surf.gii",
            hemi=["L", "R"],
        ),
        "description": "Gray matter/pial matter surface meshes.",
    },
    midthickness={
        "entities": dict(
            suffix="midthickness",
            datatype="anat",
            extension=".surf.gii",
            hemi=["L", "R"],
        ),
        "description": "Graymid/midthickness surface meshes.",
    },
    inflated={
        "entities": dict(
            suffix="inflated",
            datatype="anat",
            extension=".surf.gii",
            hemi=["L", "R"],
        ),
        "description": "Inflated surface meshes.",
    },
    # DWI
    native_dwi={
        "entities": dict(
            space=["T1w", "anat"],
            datatype="dwi",
            suffix="dwi",
            desc="preproc",
            extension=[".nii.gz", ".nii"],
        ),
        "description": "Preprocessed diffusion image in native space.",
    },
    native_bvec={
        "entities": dict(
            space=["T1w", "anat"],
            datatype="dwi",
            suffix="dwi",
            desc="preproc",
            extension=".bvec",
        ),
        "description": "Preprocessed diffusion b-vectors in native space.",
    },
    native_bval={
        "entities": dict(
            space=["T1w", "anat"],
            datatype="dwi",
            suffix="dwi",
            desc="preproc",
            extension=".bval",
        ),
        "description": "Preprocessed diffusion b-values in native space.",
    },
    native_grad={
        "entities": dict(
            space=["T1w", "anat"],
            datatype="dwi",
            suffix="dwi",
            desc="preproc",
            extension=".b",
        ),
        "description": "Preprocessed diffusion gradients in native space.",
    },
    native_dwiref={
        "entities": dict(
            space=["T1w", "anat"],
            datatype="dwi",
            suffix="mask",
            desc="brain",
            extension=[".nii.gz", ".nii"],
        ),
        "description": "Single volume DWI reference in native space.",
    },
    image_qc={
        "entities": dict(
            suffix="dwi", datatype="dwi", desc="ImageQC", extension=".csv"
        ),
        "description": "Diffusion image's preprocessing QC report.",
    },
    eddy_cnr={
        "entities": dict(
            space=["T1w", "anat"], datatype="dwi", suffix="cnr", desc="eddy"
        ),
        "description": "Eddy's CNR in native space.",
    },
    confounds_tsv={
        "entities": dict(datatype="dwi", suffix="confounds", extension=".tsv"),
        "description": "Preprocessing's confounds tsv file.",
    },
)

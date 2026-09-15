# Collection of important/interesting links

## Similar projects / pretrained models

* Exactly what we need, but for human hands, no pretrained weights [github](https://github.com/PhilipGutberlet/Xray_Handbone_Segmentation?utm_source=chatgpt.com#YOLO-Object-Detection-Model-Finetuning)
* Leg Bones, not quite as applicable, but with annotated training data [github](https://github.com/YouOnlyLiftOnce/Bone-Segmentation-and-Knee-Alignment-Analysis/tree/master/data)
* Medical Segment Anything - might be to huge for us - trained on 20 A100 80G GPUs O.o [github](https://github.com/bowang-lab/MedSAM?utm_source=chatgpt.com)
* ARAA-Net: Adaptive Region-Aware Attention Network for Epiphysis and Articular Surface Segmentation From Hand Radiographs [paper](https://www.researchgate.net/publication/379346268_ARAA-Net_Adaptive_Region-Aware_Attention_Network_for_Epiphysis_and_Articular_Surface_Segmentation_from_Hand_Radiographs) havent requested pdf, [github](https://github.com/langdecc511/ARAA-Net?utm_source=chatgpt.com), inlcudes training data and final weights
* SKELEX: musculoSKELEtal X-ray foundation model [github](https://github.com/skhoha/SKELEX?utm_source=chatgpt.com)
* Bone Segmentation, [github](https://github.com/Gulsukocak/bone-segmentation?utm_source=chatgpt.com), includes [labeled dataset ](https://drive.google.com/drive/folders/1b9hX52VOdfKuB-D4eFhWwCW7kM4wiwHL)
* Segmentation of anatomical structures in chest radiographs using supervised methods: a [comparative study ](https://www.sciencedirect.com/science/article/pii/S1361841505000368) on a public database 

## Datasets
* Standford MURA ([40k images](https://stanford.redivis.com/datasets/cv1a-apytk3j44)), "Normal"/"Abnormal" - could be used for transfer learning
* [Dataset](https://zenodo.org/records/7056076?utm_source=chatgpt.com&preview_file=masks.zip) 247 chest x-rays with segmentation
* [VinDr-RibCXR](https://github.com/vinbigdata-medical/MIDL2021-VinDr-RibCXR?utm_source=chatgpt.com): A Benchmark Dataset for Automatic Segmentation and Labeling of Individual Ribs on Chest X-rays - data upon request - website of lab is now for sale, not sure how good our chances are there
* Huge hand dataset set 1200 - including segmentations [HuggingFace](https://huggingface.co/datasets/TokyoTechMagicYang/RAM-H1200-v1)
* [CheXmask Database](https://www.physionet.org/content/chexmask-cxr-segmentation-data/1.0.0/): a large-scale dataset of anatomical segmentation masks for chest x-ray images - 657,566 anatomical segmentation masks derived from images which have been processed using the HybridGNet model
* Hand mask for the RSNA bone age [dataset](https://zenodo.org/records/7611677) - manual thresholding for masking? might not be bone level segmentation
* 

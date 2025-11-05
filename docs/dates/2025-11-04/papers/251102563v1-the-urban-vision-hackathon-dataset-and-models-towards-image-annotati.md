---
layout: default
title: The Urban Vision Hackathon Dataset and Models: Towards Image Annotations and Accurate Vision Models for Indian Traffic
---

# The Urban Vision Hackathon Dataset and Models: Towards Image Annotations and Accurate Vision Models for Indian Traffic
**arXiv**：[2511.02563v1](https://arxiv.org/abs/2511.02563) · [PDF](https://arxiv.org/pdf/2511.02563.pdf)  
**作者**：Akash Sharma, Chinmay Mhatre, Sankalp Gawali, Ruthvik Bokkasam, Brij Kishore, Vishwajeet Pattanaik, Tarun Rambha, Abdul R. Pinjari, Vijay Kovvali, Anirban Chakraborty, Punit Rathore, Raghu Krishnapuram, Yogesh Simmhan  

**一句话要点**：提出UVH-26数据集和模型，以提升印度交通场景下的目标检测准确性。

**关键词**：目标检测, 交通监控, 众包标注, 印度车辆数据集, 模型微调

## 3 点简述
- 核心问题：现有数据集缺乏印度交通多样性，影响智能交通系统部署。
- 方法要点：通过众包标注26,646张图像，生成1.8百万边界框覆盖14类印度车辆。
- 实验或效果：训练YOLO和DETR模型，mAP50:95最高达0.67，优于COCO基线8.4-31.5%。

## 摘要（原文）

> This report describes the UVH-26 dataset, the first public release by
> AIM@IISc of a large-scale dataset of annotated traffic-camera images from
> India. The dataset comprises 26,646 high-resolution (1080p) images sampled from
> 2800 Bengaluru's Safe-City CCTV cameras over a 4-week period, and subsequently
> annotated through a crowdsourced hackathon involving 565 college students from
> across India. In total, 1.8 million bounding boxes were labeled across 14
> vehicle classes specific to India: Cycle, 2-Wheeler (Motorcycle), 3-Wheeler
> (Auto-rickshaw), LCV (Light Commercial Vehicles), Van, Tempo-traveller,
> Hatchback, Sedan, SUV, MUV, Mini-bus, Bus, Truck and Other. Of these, 283k-316k
> consensus ground truth bounding boxes and labels were derived for distinct
> objects in the 26k images using Majority Voting and STAPLE algorithms. Further,
> we train multiple contemporary detectors, including YOLO11-S/X, RT-DETR-S/X,
> and DAMO-YOLO-T/L using these datasets, and report accuracy based on mAP50,
> mAP75 and mAP50:95. Models trained on UVH-26 achieve 8.4-31.5% improvements in
> mAP50:95 over equivalent baseline models trained on COCO dataset, with
> RT-DETR-X showing the best performance at 0.67 (mAP50:95) as compared to 0.40
> for COCO-trained weights for common classes (Car, Bus, and Truck). This
> demonstrates the benefits of domain-specific training data for Indian traffic
> scenarios. The release package provides the 26k images with consensus
> annotations based on Majority Voting (UVH-26-MV) and STAPLE (UVH-26-ST) and the
> 6 fine-tuned YOLO and DETR models on each of these datasets. By capturing the
> heterogeneity of Indian urban mobility directly from operational traffic-camera
> streams, UVH-26 addresses a critical gap in existing global benchmarks, and
> offers a foundation for advancing detection, classification, and deployment of
> intelligent transportation systems in emerging nations with complex traffic
> conditions.


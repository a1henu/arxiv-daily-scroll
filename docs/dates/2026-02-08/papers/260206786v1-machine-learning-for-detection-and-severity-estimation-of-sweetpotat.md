---
layout: default
title: Machine Learning for Detection and Severity Estimation of Sweetpotato Weevil Damage in Field and Lab Conditions
---

# Machine Learning for Detection and Severity Estimation of Sweetpotato Weevil Damage in Field and Lab Conditions
**arXiv**：[2602.06786v1](https://arxiv.org/abs/2602.06786) · [PDF](https://arxiv.org/pdf/2602.06786.pdf)  
**作者**：Doreen M. Chelangat, Sudi Murindanyi, Bruce Mugizi, Paul Musana, Benard Yada, Milton A. Otema, Florence Osaru, Andrew Katumba, Joyce Nakatumba-Nabende  

**一句话要点**：提出基于计算机视觉的方法，在田间和实验室条件下自动检测和评估甘薯象鼻虫损害。

**关键词**：计算机视觉, 甘薯象鼻虫检测, 对象检测, YOLO12, 田间评估, 实验室评估

## 3 点简述
- 核心问题：传统甘薯象鼻虫损害评估方法依赖人工评分，劳动密集、主观且结果不一致，阻碍育种计划。
- 方法要点：在田间使用分类模型预测损害严重程度；在实验室采用YOLO12对象检测模型，结合根部分割和分块策略提升小目标检测。
- 实验或效果：田间模型测试准确率达71.43%；实验室模型平均精度达77.7%，能有效识别微小取食孔。

## 摘要（原文）

> Sweetpotato weevils (Cylas spp.) are considered among the most destructive pests impacting sweetpotato production, particularly in sub-Saharan Africa. Traditional methods for assessing weevil damage, predominantly relying on manual scoring, are labour-intensive, subjective, and often yield inconsistent results. These challenges significantly hinder breeding programs aimed at developing resilient sweetpotato varieties. This study introduces a computer vision-based approach for the automated evaluation of weevil damage in both field and laboratory contexts. In the field settings, we collected data to train classification models to predict root-damage severity levels, achieving a test accuracy of 71.43%. Additionally, we established a laboratory dataset and designed an object detection pipeline employing YOLO12, a leading real-time detection model. This methodology incorporated a two-stage laboratory pipeline that combined root segmentation with a tiling strategy to improve the detectability of small objects. The resulting model demonstrated a mean average precision of 77.7% in identifying minute weevil feeding holes. Our findings indicate that computer vision technologies can provide efficient, objective, and scalable assessment tools that align seamlessly with contemporary breeding workflows. These advancements represent a significant improvement in enhancing phenotyping efficiency within sweetpotato breeding programs and play a crucial role in mitigating the detrimental effects of weevils on food security.


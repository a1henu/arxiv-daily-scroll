---
layout: default
title: MedImageInsight for Thoracic Cavity Health Classification from Chest X-rays
---

# MedImageInsight for Thoracic Cavity Health Classification from Chest X-rays
**arXiv**：[2511.17043v1](https://arxiv.org/abs/2511.17043) · [PDF](https://arxiv.org/pdf/2511.17043.pdf)  
**作者**：Rama Krishna Boya, Mohan Kireeti Magalanadu, Azaruddin Palavalli, Rupa Ganesh Tekuri, Amrit Pattanayak, Prasanthi Enuga, Vignesh Esakki Muthu, Vivek Aditya Boya  

**一句话要点**：提出MedImageInsight模型用于胸部X光片正常与异常二元分类，以减轻放射科医生负担。

**关键词**：胸部X光分类, 医学影像基础模型, 二元分类, ROC-AUC评估, 临床工作流集成

## 3 点简述
- 核心问题：胸部X光片解读工作量大，需自动化分类以支持及时诊断。
- 方法要点：评估微调MedImageInsight和特征提取结合传统分类器两种方法。
- 实验或效果：微调模型ROC-AUC达0.888，性能与CheXNet相当，适用于临床集成。

## 摘要（原文）

> Chest radiography remains one of the most widely used imaging modalities for thoracic diagnosis, yet increasing imaging volumes and radiologist workload continue to challenge timely interpretation. In this work, we investigate the use of MedImageInsight, a medical imaging foundational model, for automated binary classification of chest X-rays into Normal and Abnormal categories. Two approaches were evaluated: (1) fine-tuning MedImageInsight for end-to-end classification, and (2) employing the model as a feature extractor for a transfer learning pipeline using traditional machine learning classifiers. Experiments were conducted using a combination of the ChestX-ray14 dataset and real-world clinical data sourced from partner hospitals. The fine-tuned classifier achieved the highest performance, with an ROC-AUC of 0.888 and superior calibration compared to the transfer learning models, demonstrating performance comparable to established architectures such as CheXNet. These results highlight the effectiveness of foundational medical imaging models in reducing task-specific training requirements while maintaining diagnostic reliability. The system is designed for integration into web-based and hospital PACS workflows to support triage and reduce radiologist burden. Future work will extend the model to multi-label pathology classification to provide preliminary diagnostic interpretation in clinical environments.


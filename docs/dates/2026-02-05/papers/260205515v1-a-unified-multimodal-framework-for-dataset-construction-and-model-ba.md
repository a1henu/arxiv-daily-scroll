---
layout: default
title: A Unified Multimodal Framework for Dataset Construction and Model-Based Diagnosis of Ameloblastoma
---

# A Unified Multimodal Framework for Dataset Construction and Model-Based Diagnosis of Ameloblastoma
**arXiv**：[2602.05515v1](https://arxiv.org/abs/2602.05515) · [PDF](https://arxiv.org/pdf/2602.05515.pdf)  
**作者**：Ajo Babu George, Anna Mariam John, Athul Anoop, Balu Bhasuran  

**一句话要点**：提出统一多模态框架以构建数据集并支持成釉细胞瘤的诊断与个性化决策。

**关键词**：多模态数据集, 成釉细胞瘤诊断, 深度学习模型, 自然语言处理, 个性化医疗, 颌面病理学

## 3 点简述
- 核心问题：现有数据集对成釉细胞瘤覆盖有限且格式不一致，阻碍AI在颌面病理学中的直接应用。
- 方法要点：整合标注的放射学、组织病理学和临床图像，利用自然语言处理提取文本特征，开发多模态深度学习模型。
- 实验或效果：模型将变异分类准确率从46.2%提升至65.9%，异常组织检测F1分数从43.0%提升至90.3%。

## 摘要（原文）

> Artificial intelligence (AI)-enabled diagnostics in maxillofacial pathology require structured, high-quality multimodal datasets. However, existing resources provide limited ameloblastoma coverage and lack the format consistency needed for direct model training. We present a newly curated multimodal dataset specifically focused on ameloblastoma, integrating annotated radiological, histopathological, and intraoral clinical images with structured data derived from case reports. Natural language processing techniques were employed to extract clinically relevant features from textual reports, while image data underwent domain specific preprocessing and augmentation. Using this dataset, a multimodal deep learning model was developed to classify ameloblastoma variants, assess behavioral patterns such as recurrence risk, and support surgical planning. The model is designed to accept clinical inputs such as presenting complaint, age, and gender during deployment to enhance personalized inference. Quantitative evaluation demonstrated substantial improvements; variant classification accuracy increased from 46.2 percent to 65.9 percent, and abnormal tissue detection F1-score improved from 43.0 percent to 90.3 percent. Benchmarked against resources like MultiCaRe, this work advances patient-specific decision support by providing both a robust dataset and an adaptable multimodal AI framework.


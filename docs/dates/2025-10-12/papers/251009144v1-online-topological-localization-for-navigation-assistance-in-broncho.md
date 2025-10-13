---
layout: default
title: Online Topological Localization for Navigation Assistance in Bronchoscopy
---

# Online Topological Localization for Navigation Assistance in Bronchoscopy
**arXiv**：[2510.09144v1](https://arxiv.org/abs/2510.09144) · [PDF](https://arxiv.org/pdf/2510.09144.pdf)  
**作者**：Clara Tomasini, Luis Riazuelo, Ana C. Murillo  
**一句话要点**：提出基于图像的支气管镜拓扑定位方法，用于术中导航辅助，无需患者CT扫描。
**关键词**：支气管镜导航, 拓扑定位, 图像处理, 医学影像, 无CT扫描, 泛化能力

## 3 点简述
- 支气管镜检查中，医生难以在复杂气道中定位内窥镜位置，影响诊断和手术效果。
- 方法使用图像处理进行拓扑定位，仅需通用气道模型训练，无需患者特定CT数据。
- 在真实数据测试中表现优于现有方法，具有良好的泛化能力。

## 摘要（原文）

> Video bronchoscopy is a fundamental procedure in respiratory medicine, where
> medical experts navigate through the bronchial tree of a patient to diagnose or
> operate the patient. Surgeons need to determine the position of the scope as
> they go through the airway until they reach the area of interest. This task is
> very challenging for practitioners due to the complex bronchial tree structure
> and varying doctor experience and training. Navigation assistance to locate the
> bronchoscope during the procedure can improve its outcome. Currently used
> techniques for navigational guidance commonly rely on previous CT scans of the
> patient to obtain a 3D model of the airway, followed by tracking of the scope
> with additional sensors or image registration. These methods obtain accurate
> locations but imply additional setup, scans and training. Accurate metric
> localization is not always required, and a topological localization with regard
> to a generic airway model can often suffice to assist the surgeon with
> navigation. We present an image-based bronchoscopy topological localization
> pipeline to provide navigation assistance during the procedure, with no need of
> patient CT scan. Our approach is trained only on phantom data, eliminating the
> high cost of real data labeling, and presents good generalization capabilities.
> The results obtained surpass existing methods, particularly on real data test
> sequences.


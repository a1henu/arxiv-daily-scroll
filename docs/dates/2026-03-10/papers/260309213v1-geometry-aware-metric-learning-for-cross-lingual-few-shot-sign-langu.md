---
layout: default
title: Geometry-Aware Metric Learning for Cross-Lingual Few-Shot Sign Language Recognition on Static Hand Keypoints
---

# Geometry-Aware Metric Learning for Cross-Lingual Few-Shot Sign Language Recognition on Static Hand Keypoints
**arXiv**：[2603.09213v1](https://arxiv.org/abs/2603.09213) · [PDF](https://arxiv.org/pdf/2603.09213.pdf)  
**作者**：Chayanin Chamachot, Kanokphan Lertniponphan  

**一句话要点**：提出基于几何不变角度的度量学习框架，用于跨语言少样本手语识别，以应对数据稀缺和域偏移问题。

**关键词**：手语识别, 少样本学习, 跨语言迁移, 几何不变特征, 度量学习, 静态手关键点

## 3 点简述
- 核心问题：跨语言少样本手语识别中，基于坐标的关键点表示易受相机视角、手部尺度和录制条件差异导致的域偏移影响，影响原型稳定性。
- 方法要点：使用从MediaPipe静态手关键点导出的20维关节间角度描述符，该描述符对SO(3)旋转、平移和各向同性缩放不变，消除主要域偏移源。
- 实验或效果：在四种手语字母表上评估，角度特征比归一化坐标基线提升高达25个百分点，跨语言迁移常优于域内准确率，参数约10^5。

## 摘要（原文）

> Sign language recognition (SLR) systems typically require large labeled corpora for each language, yet the majority of the world's 300+ sign languages lack sufficient annotated data. Cross-lingual few-shot transfer, pretraining on a data-rich source language and adapting with only a handful of target-language examples, offers a scalable alternative, but conventional coordinate-based keypoint representations are susceptible to domain shift arising from differences in camera viewpoint, hand scale, and recording conditions. This shift is particularly detrimental in the few-shot regime, where class prototypes estimated from only K examples are highly sensitive to extrinsic variance. We propose a geometry-aware metric-learning framework centered on a compact 20-dimensional inter-joint angle descriptor derived from MediaPipe static hand keypoints. These angles are invariant to SO(3) rotation, translation, and isotropic scaling, eliminating the dominant sources of cross-dataset shift and yielding tighter, more stable class prototypes. Evaluated on four fingerspelling alphabets spanning typologically diverse sign languages, ASL, LIBRAS, Arabic Sign Language, and Thai Sign Language, the proposed angle features improve over normalized-coordinate baselines by up to 25 percentage points within-domain and enable frozen cross-lingual transfer that frequently exceeds within-domain accuracy, using a lightweight MLP encoder with about 10^5 parameters. These findings demonstrate that invariant hand-geometry descriptors provide a portable and effective foundation for cross-lingual few-shot SLR in low-resource settings.


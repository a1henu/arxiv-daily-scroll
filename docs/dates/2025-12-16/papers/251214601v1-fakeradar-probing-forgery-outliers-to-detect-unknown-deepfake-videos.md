---
layout: default
title: FakeRadar: Probing Forgery Outliers to Detect Unknown Deepfake Videos
---

# FakeRadar: Probing Forgery Outliers to Detect Unknown Deepfake Videos
**arXiv**：[2512.14601v1](https://arxiv.org/abs/2512.14601) · [PDF](https://arxiv.org/pdf/2512.14601.pdf)  
**作者**：Zhaolun Li, Jichang Li, Yinqi Cai, Junye Chen, Xiaonan Luo, Guanbin Li, Rushi Lan  

**一句话要点**：提出FakeRadar框架以解决深度伪造视频检测中的跨域泛化挑战

**关键词**：深度伪造检测, 跨域泛化, 异常探测, 对比学习, 视频伪造识别

## 3 点简述
- 核心问题：现有方法依赖已知伪造线索，对新兴伪造技术泛化能力差
- 方法要点：通过伪造异常探测模拟未知伪造模式，结合异常引导三训练优化检测器
- 实验或效果：在多个基准数据集上优于现有方法，尤其在跨域评估中表现突出

## 摘要（原文）

> In this paper, we propose FakeRadar, a novel deepfake video detection framework designed to address the challenges of cross-domain generalization in real-world scenarios. Existing detection methods typically rely on manipulation-specific cues, performing well on known forgery types but exhibiting severe limitations against emerging manipulation techniques. This poor generalization stems from their inability to adapt effectively to unseen forgery patterns. To overcome this, we leverage large-scale pretrained models (e.g. CLIP) to proactively probe the feature space, explicitly highlighting distributional gaps between real videos, known forgeries, and unseen manipulations. Specifically, FakeRadar introduces Forgery Outlier Probing, which employs dynamic subcluster modeling and cluster-conditional outlier generation to synthesize outlier samples near boundaries of estimated subclusters, simulating novel forgery artifacts beyond known manipulation types. Additionally, we design Outlier-Guided Tri-Training, which optimizes the detector to distinguish real, fake, and outlier samples using proposed outlier-driven contrastive learning and outlier-conditioned cross-entropy losses. Experiments show that FakeRadar outperforms existing methods across various benchmark datasets for deepfake video detection, particularly in cross-domain evaluations, by handling the variety of emerging manipulation techniques.


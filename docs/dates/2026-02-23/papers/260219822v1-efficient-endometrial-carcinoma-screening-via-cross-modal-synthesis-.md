---
layout: default
title: Efficient endometrial carcinoma screening via cross-modal synthesis and gradient distillation
---

# Efficient endometrial carcinoma screening via cross-modal synthesis and gradient distillation
**arXiv**：[2602.19822v1](https://arxiv.org/abs/2602.19822) · [PDF](https://arxiv.org/pdf/2602.19822.pdf)  
**作者**：Dongjing Shan, Yamei Luo, Jiqing Xuan, Lu Huang, Jin Li, Mengchu Yang, Zeyu Chen, Fajin Lv, Yong Tang, Chunxiang Zhang  

**一句话要点**：提出基于跨模态合成与梯度蒸馏的高效深度学习框架，以解决资源受限基层医疗中子宫内膜癌筛查的数据与计算瓶颈。

**关键词**：子宫内膜癌筛查, 跨模态合成, 梯度蒸馏, 轻量级网络, 医学影像分析, 深度学习框架

## 3 点简述
- 核心问题：子宫内膜癌筛查中，经阴道超声因组织对比度低、操作依赖性强及阳性样本稀缺，导致诊断可靠性受限，现有AI方法难以克服类别不平衡和计算限制。
- 方法要点：开发结构引导的跨模态生成网络，从非配对MRI合成高保真超声图像，并引入轻量级筛查网络，通过梯度蒸馏从大容量教师模型转移判别知识，动态聚焦关键区域。
- 实验或效果：在7,951名参与者的多中心队列中，模型以0.289 GFLOPs计算成本实现99.5%灵敏度、97.2%特异性和0.987 AUC，显著超越专家超声医师平均诊断准确率。

## 摘要（原文）

> Early detection of myometrial invasion is critical for the staging and life-saving management of endometrial carcinoma (EC), a prevalent global malignancy. Transvaginal ultrasound serves as the primary, accessible screening modality in resource-constrained primary care settings; however, its diagnostic reliability is severely hindered by low tissue contrast, high operator dependence, and a pronounced scarcity of positive pathological samples. Existing artificial intelligence solutions struggle to overcome this severe class imbalance and the subtle imaging features of invasion, particularly under the strict computational limits of primary care clinics. Here we present an automated, highly efficient two-stage deep learning framework that resolves both data and computational bottlenecks in EC screening. To mitigate pathological data scarcity, we develop a structure-guided cross-modal generation network that synthesizes diverse, high-fidelity ultrasound images from unpaired magnetic resonance imaging (MRI) data, strictly preserving clinically essential anatomical junctions. Furthermore, we introduce a lightweight screening network utilizing gradient distillation, which transfers discriminative knowledge from a high-capacity teacher model to dynamically guide sparse attention towards task-critical regions. Evaluated on a large, multicenter cohort of 7,951 participants, our model achieves a sensitivity of 99.5\%, a specificity of 97.2\%, and an area under the curve of 0.987 at a minimal computational cost (0.289 GFLOPs), substantially outperforming the average diagnostic accuracy of expert sonographers. Our approach demonstrates that combining cross-modal synthetic augmentation with knowledge-driven efficient modeling can democratize expert-level, real-time cancer screening for resource-constrained primary care settings.


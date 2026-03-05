---
layout: default
title: GarmentPile++: Affordance-Driven Cluttered Garments Retrieval with Vision-Language Reasoning
---

# GarmentPile++: Affordance-Driven Cluttered Garments Retrieval with Vision-Language Reasoning
**arXiv**：[2603.04158v1](https://arxiv.org/abs/2603.04158) · [PDF](https://arxiv.org/pdf/2603.04158.pdf)  
**作者**：Mingleyang Li, Yuran Wang, Yue Chen, Tianxing Chen, Jiaqi Liang, Zishun Shen, Haoran Lu, Ruihai Wu, Hao Dong  

**一句话要点**：提出GarmentPile++以解决现实场景中堆叠衣物检索问题，通过视觉语言推理与视觉可供性感知实现安全、精准的单件衣物抓取。

**关键词**：衣物检索, 视觉语言推理, 视觉可供性, 堆叠衣物, 双臂协作, 掩码微调

## 3 点简述
- 核心问题：现有衣物操纵研究多假设单件衣物初始状态，而现实场景中衣物常堆叠，导致检索困难。
- 方法要点：结合视觉语言模型进行高层推理与视觉可供性感知执行低层动作，利用SAM2分割增强视觉线索，并引入掩码微调与双臂协作框架。
- 实验或效果：在真实与仿真环境中验证了管道在多样化任务和场景中的有效性，确保每次尝试仅检索一件衣物。

## 摘要（原文）

> Garment manipulation has attracted increasing attention due to its critical role in home-assistant robotics. However, the majority of existing garment manipulation works assume an initial state consisting of only one garment, while piled garments are far more common in real-world settings. To bridge this gap, we propose a novel garment retrieval pipeline that can not only follow language instruction to execute safe and clean retrieval but also guarantee exactly one garment is retrieved per attempt, establishing a robust foundation for the execution of downstream tasks (e.g., folding, hanging, wearing). Our pipeline seamlessly integrates vision-language reasoning with visual affordance perception, fully leveraging the high-level reasoning and planning capabilities of VLMs alongside the generalization power of visual affordance for low-level actions. To enhance the VLM's comprehensive awareness of each garment's state within a garment pile, we employ visual segmentation model (SAM2) to execute object segmentation on the garment pile for aiding VLM-based reasoning with sufficient visual cues. A mask fine-tuning mechanism is further integrated to address scenarios where the initial segmentation results are suboptimal. In addition, a dual-arm cooperation framework is deployed to address cases involving large or long garments, as well as excessive garment sagging caused by incorrect grasping point determination, both of which are strenuous for a single arm to handle. The effectiveness of our pipeline are consistently demonstrated across diverse tasks and varying scenarios in both real-world and simulation environments. Project page: https://garmentpile2.github.io/.


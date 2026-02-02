---
layout: default
title: Deep in the Jungle: Towards Automating Chimpanzee Population Estimation
---

# Deep in the Jungle: Towards Automating Chimpanzee Population Estimation
**arXiv**：[2601.22917v1](https://arxiv.org/abs/2601.22917) · [PDF](https://arxiv.org/pdf/2601.22917.pdf)  
**作者**：Tom Raynes, Otto Brookes, Timm Haucke, Lukas Bösch, Anne-Sophie Crunchant, Hjalmar Kühl, Sara Beery, Majid Mirmehdi, Tilo Burghardt  

**一句话要点**：提出基于单目深度估计的相机陷阱距离采样方法，用于黑猩猩种群自动估算

**关键词**：单目深度估计, 相机陷阱, 种群密度估算, 黑猩猩保护, 计算机视觉生态学

## 3 点简述
- 核心问题：传统黑猩猩种群估算依赖人工测量动物到相机距离，劳动密集且效率低。
- 方法要点：集成DPT和Depth Anything模型，结合多种距离采样策略，自动估计检测距离。
- 实验或效果：在220个真实视频上评估，校准DPT优于Depth Anything，估算结果与传统方法偏差在22%内。

## 摘要（原文）

> The estimation of abundance and density in unmarked populations of great apes relies on statistical frameworks that require animal-to-camera distance measurements. In practice, acquiring these distances depends on labour-intensive manual interpretation of animal observations across large camera trap video corpora. This study introduces and evaluates an only sparsely explored alternative: the integration of computer vision-based monocular depth estimation (MDE) pipelines directly into ecological camera trap workflows for great ape conservation. Using a real-world dataset of 220 camera trap videos documenting a wild chimpanzee population, we combine two MDE models, Dense Prediction Transformers and Depth Anything, with multiple distance sampling strategies. These components are used to generate detection distance estimates, from which population density and abundance are inferred. Comparative analysis against manually derived ground-truth distances shows that calibrated DPT consistently outperforms Depth Anything. This advantage is observed in both distance estimation accuracy and downstream density and abundance inference. Nevertheless, both models exhibit systematic biases. We show that, given complex forest environments, they tend to overestimate detection distances and consequently underestimate density and abundance relative to conventional manual approaches. We further find that failures in animal detection across distance ranges are a primary factor limiting estimation accuracy. Overall, this work provides a case study that shows MDE-driven camera trap distance sampling is a viable and practical alternative to manual distance estimation. The proposed approach yields population estimates within 22% of those obtained using traditional methods.


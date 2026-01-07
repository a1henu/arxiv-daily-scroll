---
layout: default
title: ReCCur: A Recursive Corner-Case Curation Framework for Robust Vision-Language Understanding in Open and Edge Scenarios
---

# ReCCur: A Recursive Corner-Case Curation Framework for Robust Vision-Language Understanding in Open and Edge Scenarios
**arXiv**：[2601.03011v1](https://arxiv.org/abs/2601.03011) · [PDF](https://arxiv.org/pdf/2601.03011.pdf)  
**作者**：Yihan Wei, Shenghai Yuan, Tianchen Deng, Boyang Lou, Enwen Hu  

**一句话要点**：提出ReCCur框架，通过递归多代理流程将噪声网络图像转化为可审计细粒度标签，以增强开放和边缘场景下的视觉语言理解鲁棒性。

**关键词**：角案例整理, 视觉语言模型, 知识蒸馏, 对抗标注, 边缘计算, 鲁棒性增强

## 3 点简述
- 核心问题：角案例（罕见或极端场景）难以大规模整理，网络数据噪声大、标签脆弱，边缘部署限制重训练。
- 方法要点：采用多代理递归管道，包括数据获取与过滤、专家混合知识蒸馏和区域证据VLM对抗标注，实现低计算量标签生成。
- 实验或效果：在真实角案例场景（如淹水车辆检测）中，ReCCur在消费级GPU上运行，提升纯度和可分离性，需最小人工监督。

## 摘要（原文）

> Corner cases are rare or extreme scenarios that drive real-world failures, but they are difficult to curate at scale: web data are noisy, labels are brittle, and edge deployments preclude large retraining. We present ReCCur (Recursive Corner-Case Curation), a low-compute framework that converts noisy web imagery into auditable fine-grained labels via a multi-agent recursive pipeline. First, large-scale data acquisition and filtering expands a domain vocabulary with a vision-language model (VLM), crawls the web, and enforces tri-modal (image, description, keyword) consistency with light human spot checks to yield refined candidates. Next, mixture-of-experts knowledge distillation uses complementary encoders (e.g., CLIP, DINOv2, BEiT) for kNN voting with dual-confidence activation and uncertainty sampling, converging to a high-precision set. Finally, region-evidence VLM adversarial labeling pairs a proposer (multi-granularity regions and semantic cues) with a validator (global and local chained consistency) to produce explainable labels and close the loop. On realistic corner-case scenarios (e.g., flooded-car inspection), ReCCur runs on consumer-grade GPUs, steadily improves purity and separability, and requires minimal human supervision, providing a practical substrate for downstream training and evaluation under resource constraints. Code and dataset will be released.


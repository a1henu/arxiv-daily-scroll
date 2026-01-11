---
layout: default
title: AIVD: Adaptive Edge-Cloud Collaboration for Accurate and Efficient Industrial Visual Detection
---

# AIVD: Adaptive Edge-Cloud Collaboration for Accurate and Efficient Industrial Visual Detection
**arXiv**：[2601.04734v1](https://arxiv.org/abs/2601.04734) · [PDF](https://arxiv.org/pdf/2601.04734.pdf)  
**作者**：Yunqing Hu, Zheming Yang, Chang Zhao, Qi Guo, Meng Gao, Pengcheng Li, Wen Ji  

**一句话要点**：提出AIVD框架，通过边缘-云协作实现工业视觉检测的精准定位与高效部署。

**关键词**：边缘-云协作, 工业视觉检测, 多模态大语言模型, 动态调度算法, 视觉-语义增强

## 3 点简述
- 核心问题：MLLMs在精准定位和资源受限边缘部署中面临挑战。
- 方法要点：结合轻量边缘检测器和云MLLMs，设计视觉-语义协同增强微调策略。
- 实验或效果：显著提升分类精度和语义一致性，降低资源消耗和延迟。

## 摘要（原文）

> Multimodal large language models (MLLMs) demonstrate exceptional capabilities in semantic understanding and visual reasoning, yet they still face challenges in precise object localization and resource-constrained edge-cloud deployment. To address this, this paper proposes the AIVD framework, which achieves unified precise localization and high-quality semantic generation through the collaboration between lightweight edge detectors and cloud-based MLLMs. To enhance the cloud MLLM's robustness against edge cropped-box noise and scenario variations, we design an efficient fine-tuning strategy with visual-semantic collaborative augmentation, significantly improving classification accuracy and semantic consistency. Furthermore, to maintain high throughput and low latency across heterogeneous edge devices and dynamic network conditions, we propose a heterogeneous resource-aware dynamic scheduling algorithm. Experimental results demonstrate that AIVD substantially reduces resource consumption while improving MLLM classification performance and semantic generation quality. The proposed scheduling strategy also achieves higher throughput and lower latency across diverse scenarios.


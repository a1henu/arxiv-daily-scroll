---
layout: default
title: Co-Training Vision Language Models for Remote Sensing Multi-task Learning
---

# Co-Training Vision Language Models for Remote Sensing Multi-task Learning
**arXiv**：[2511.21272v1](https://arxiv.org/abs/2511.21272) · [PDF](https://arxiv.org/pdf/2511.21272.pdf)  
**作者**：Qingyun Li, Shuran Ma, Junwei Luo, Yi Yu, Yue Zhou, Fengxiang Wang, Xudong Lu, Xiaoxing Wang, Xin He, Yushi Chen, Xue Yang, Junchi Yan  

**一句话要点**：提出RSCoVLM以解决遥感多任务学习中的数据、分辨率与检测挑战

**关键词**：遥感视觉语言模型, 多任务学习, 动态分辨率, 对象检测, 数据引擎, Zoom-in Chain

## 3 点简述
- 核心问题：遥感数据环境复杂，图像尺度多样，多任务学习需统一处理
- 方法要点：构建数据引擎、动态分辨率策略和Zoom-in Chain机制，提升检测能力
- 实验或效果：在多个任务中达到SOTA，性能优于现有VLM并接近专家模型

## 摘要（原文）

> With Transformers achieving outstanding performance on individual remote sensing (RS) tasks, we are now approaching the realization of a unified model that excels across multiple tasks through multi-task learning (MTL). Compared to single-task approaches, MTL methods offer improved generalization, enhanced scalability, and greater practical applicability. Recently, vision language models (VLMs) have achieved promising results in RS image understanding, grounding, and ultra-high-resolution (UHR) image reasoning, respectively. Moreover, the unified text-based interface demonstrates significant potential for MTL. Hence, in this work, we present RSCoVLM, a simple yet flexible VLM baseline for RS MTL. Firstly, we create the data curation engine, including data acquisition, offline processing and integrating, as well as online loading and weighting. This data engine effectively addresses complex RS data enviroment and generates flexible vision-language conversations. Furthermore, we propose a unified dynamic-resolution strategy to address the diverse image scales inherent in RS imagery. For UHR images, we introduce the Zoom-in Chain mechanism together with its corresponding dataset, LRS-VQA-Zoom. The strategies are flexible and effectively mitigate the computational burdens. Additionally, we significantly enhance the model's object detection capability and propose a novel evaluation protocol that ensures fair comparison between VLMs and conventional detection models. Extensive experiments demonstrate that RSCoVLM achieves state-of-the-art performance across diverse tasks, outperforming existing RS VLMs and even rivaling specialized expert models. All the training and evaluating tools, model weights, and datasets have been fully open-sourced to support reproducibility. We expect that this baseline will promote further progress toward general-purpose RS models.


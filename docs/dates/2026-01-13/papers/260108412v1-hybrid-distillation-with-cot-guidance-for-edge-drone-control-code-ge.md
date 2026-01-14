---
layout: default
title: Hybrid Distillation with CoT Guidance for Edge-Drone Control Code Generation
---

# Hybrid Distillation with CoT Guidance for Edge-Drone Control Code Generation
**arXiv**：[2601.08412v1](https://arxiv.org/abs/2601.08412) · [PDF](https://arxiv.org/pdf/2601.08412.pdf)  
**作者**：Yizhan Feng, Hichem Snoussi, Yuhang Wang, Jing Teng, Abel Cherouat, Tian Wang  

**一句话要点**：提出混合蒸馏与思维链引导方法，以解决无人机边缘控制代码生成中模型轻量化与性能平衡问题

**关键词**：无人机控制代码生成, 知识蒸馏, 思维链引导, 轻量化模型, 边缘计算

## 3 点简述
- 核心问题：大语言模型资源消耗高与无人机平台实时轻量需求矛盾，阻碍边缘部署
- 方法要点：结合知识蒸馏、思维链引导和监督微调，构建高质量数据集并采用混合蒸馏策略
- 实验或效果：蒸馏后轻量模型保持高代码生成准确率，显著提升部署和推理效率

## 摘要（原文）

> With large language models demonstrating significant potential in code generation tasks, their application to onboard control of resource-constrained Unmanned Aerial Vehicles has emerged as an important research direction. However, a notable contradiction exists between the high resource consumption of large models and the real-time, lightweight requirements of UAV platforms. This paper proposes an integrated approach that combines knowledge distillation, chain-of-thought guidance, and supervised fine-tuning for UAV multi-SDK control tasks, aiming to efficiently transfer complex reasoning and code generation capabilities to smaller models. Firstly, a high-quality dataset covering various mainstream UAV SDKs is constructed, featuring instruction-code-reasoning chains, and incorporates counterfactual negative samples for data augmentation, guiding the model to learn the end-to-end logic from instruction parsing to code generation. Secondly, leveraging DeepSeek-Coder-V2-Lite quantized via QLoRA as the teacher model, and based on a hybrid black-box and white-box distillation strategy, high-quality chain-of-thought soft labels are generated. These are combined with a weighted cross-entropy loss using hard labels to transfer complex reasoning capabilities to the smaller student model. Finally, through prompt tuning engineering optimized for the UAV control scenario, the model performance on core tasks such as SDK type recognition and function call matching is enhanced. Experimental results indicate that the distilled lightweight model maintains high code generation accuracy while achieving significant improvements in deployment and inference efficiency, effectively demonstrating the feasibility and superiority of our approach in achieving precise and lightweight intelligent control for UAVs


---
layout: default
title: Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models
---

# Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models
**arXiv**：[2602.01834v1](https://arxiv.org/abs/2602.01834) · [PDF](https://arxiv.org/pdf/2602.01834.pdf)  
**作者**：Siqi Wen, Shu Yang, Shaopeng Fu, Jingfeng Zhang, Lijie Hu, Di Wang  

**一句话要点**：提出基于概念的字典学习框架，以在推理时控制视觉语言动作模型的安全风险。

**关键词**：视觉语言动作模型, 推理时安全控制, 字典学习, 概念方向识别, 多模态安全, 即插即用框架

## 3 点简述
- 核心问题：VLA模型将多模态指令转化为可执行行为，放大安全风险，现有防御方法干预过晚或模态不当。
- 方法要点：从隐藏激活构建稀疏可解释字典，识别有害概念方向，应用基于阈值的干预抑制不安全激活。
- 实验或效果：在多个数据集上实现最先进防御性能，攻击成功率降低超70%，同时保持任务成功率，框架为即插即用且模型无关。

## 摘要（原文）

> Vision Language Action (VLA) models close the perception action loop by translating multimodal instructions into executable behaviors, but this very capability magnifies safety risks: jailbreaks that merely yield toxic text in LLMs can trigger unsafe physical actions in embodied systems. Existing defenses alignment, filtering, or prompt hardening intervene too late or at the wrong modality, leaving fused representations exploitable. We introduce a concept-based dictionary learning framework for inference-time safety control. By constructing sparse, interpretable dictionaries from hidden activations, our method identifies harmful concept directions and applies threshold-based interventions to suppress or block unsafe activations. Experiments on Libero-Harm, BadRobot, RoboPair, and IS-Bench show that our approach achieves state-of-the-art defense performance, cutting attack success rates by over 70\% while maintaining task success. Crucially, the framework is plug-in and model-agnostic, requiring no retraining and integrating seamlessly with diverse VLAs. To our knowledge, this is the first inference-time concept-based safety method for embodied systems, advancing both interpretability and safe deployment of VLA models.


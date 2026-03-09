---
layout: default
title: BEVLM: Distilling Semantic Knowledge from LLMs into Bird's-Eye View Representations
---

# BEVLM: Distilling Semantic Knowledge from LLMs into Bird's-Eye View Representations
**arXiv**：[2603.06576v1](https://arxiv.org/abs/2603.06576) · [PDF](https://arxiv.org/pdf/2603.06576.pdf)  
**作者**：Thomas Monninger, Shaoyuan Xie, Qi Alfred Chen, Sihao Ding  

**一句话要点**：提出BEVLM框架，通过蒸馏LLM语义知识到BEV表示以提升自动驾驶场景的推理能力。

**关键词**：自动驾驶, 鸟瞰图表示, 大语言模型, 知识蒸馏, 空间一致性, 端到端驾驶

## 3 点简述
- 现有方法独立处理多视图图像，导致计算冗余和空间一致性不足，影响3D推理。
- BEVLM连接空间一致的BEV表示与LLM，利用BEV特征作为统一输入，增强跨视图推理。
- 实验显示，BEVLM在跨视图场景中提升准确率46%，在安全关键场景中端到端驾驶性能提升29%。

## 摘要（原文）

> The integration of Large Language Models (LLMs) into autonomous driving has attracted growing interest for their strong reasoning and semantic understanding abilities, which are essential for handling complex decision-making and long-tail scenarios. However, existing methods typically feed LLMs with tokens from multi-view and multi-frame images independently, leading to redundant computation and limited spatial consistency. This separation in visual processing hinders accurate 3D spatial reasoning and fails to maintain geometric coherence across views. On the other hand, Bird's-Eye View (BEV) representations learned from geometrically annotated tasks (e.g., object detection) provide spatial structure but lack the semantic richness of foundation vision encoders. To bridge this gap, we propose BEVLM, a framework that connects a spatially consistent and semantically distilled BEV representation with LLMs. Through extensive experiments, we show that BEVLM enables LLMs to reason more effectively in cross-view driving scenes, improving accuracy by 46%, by leveraging BEV features as unified inputs. Furthermore, by distilling semantic knowledge from LLMs into BEV representations, BEVLM significantly improves closed-loop end-to-end driving performance by 29% in safety-critical scenarios.


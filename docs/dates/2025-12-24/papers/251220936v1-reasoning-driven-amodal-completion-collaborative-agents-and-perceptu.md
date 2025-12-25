---
layout: default
title: Reasoning-Driven Amodal Completion: Collaborative Agents and Perceptual Evaluation
---

# Reasoning-Driven Amodal Completion: Collaborative Agents and Perceptual Evaluation
**arXiv**：[2512.20936v1](https://arxiv.org/abs/2512.20936) · [PDF](https://arxiv.org/pdf/2512.20936.pdf)  
**作者**：Hongxing Fan, Shuyu Zhao, Jiayang Ao, Lu Sheng  

**一句话要点**：提出协作多智能体推理框架以解决无模态补全中的语义一致性和结构完整性问题。

**关键词**：无模态补全, 多智能体推理, 语义规划, 视觉合成, 评估指标, 结构完整性

## 3 点简述
- 核心问题：无模态补全任务面临语义不一致和结构不完整的挑战，现有渐进方法存在推理不稳定和误差累积。
- 方法要点：通过解耦语义规划和视觉合成，采用专门智能体进行前期推理，生成结构化计划，并集成自校正验证和多样假设生成机制。
- 实验或效果：在多个数据集上显著优于现有方法，并引入MAC-Score作为新评估指标，验证了结构完整性和语义一致性。

## 摘要（原文）

> Amodal completion, the task of inferring invisible object parts, faces significant challenges in maintaining semantic consistency and structural integrity. Prior progressive approaches are inherently limited by inference instability and error accumulation. To tackle these limitations, we present a Collaborative Multi-Agent Reasoning Framework that explicitly decouples Semantic Planning from Visual Synthesis. By employing specialized agents for upfront reasoning, our method generates a structured, explicit plan before pixel generation, enabling visually and semantically coherent single-pass synthesis. We integrate this framework with two critical mechanisms: (1) a self-correcting Verification Agent that employs Chain-of-Thought reasoning to rectify visible region segmentation and identify residual occluders strictly within the Semantic Planning phase, and (2) a Diverse Hypothesis Generator that addresses the ambiguity of invisible regions by offering diverse, plausible semantic interpretations, surpassing the limited pixel-level variations of standard random seed sampling. Furthermore, addressing the limitations of traditional metrics in assessing inferred invisible content, we introduce the MAC-Score (MLLM Amodal Completion Score), a novel human-aligned evaluation metric. Validated against human judgment and ground truth, these metrics establish a robust standard for assessing structural completeness and semantic consistency with visible context. Extensive experiments demonstrate that our framework significantly outperforms state-of-the-art methods across multiple datasets. Our project is available at: https://fanhongxing.github.io/remac-page.


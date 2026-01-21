---
layout: default
title: TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers
---

# TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers
**arXiv**：[2601.14133v1](https://arxiv.org/abs/2601.14133) · [PDF](https://arxiv.org/pdf/2601.14133.pdf)  
**作者**：Bin Yu, Shijie Lian, Xiaopeng Lin, Yuliang Wei, Zhaolong Shen, Changti Wu, Yuzhuo Miao, Xinming Wang, Bailing Wang, Cong Huang, Kai Chen  

**一句话要点**：提出TwinBrainVLA架构，通过非对称混合Transformer解决VLA模型在具身任务中通用语义理解与精细运动技能间的冲突。

**关键词**：具身智能, 视觉-语言-动作模型, 非对称混合Transformer, 灾难性遗忘, 机器人控制, 通用语义理解

## 3 点简述
- 标准VLA模型在微调时易导致通用语义理解能力退化，引发灾难性遗忘问题。
- TwinBrainVLA采用非对称混合Transformer机制，协调冻结的通用VLM与可训练的专用VLM进行联合控制。
- 在SimplerEnv和RoboCasa基准测试中，模型在保持通用视觉理解的同时，实现了优越的操控性能。

## 摘要（原文）

> Standard Vision-Language-Action (VLA) models typically fine-tune a monolithic Vision-Language Model (VLM) backbone explicitly for robotic control. However, this approach creates a critical tension between maintaining high-level general semantic understanding and learning low-level, fine-grained sensorimotor skills, often leading to "catastrophic forgetting" of the model's open-world capabilities. To resolve this conflict, we introduce TwinBrainVLA, a novel architecture that coordinates a generalist VLM retaining universal semantic understanding and a specialist VLM dedicated to embodied proprioception for joint robotic control. TwinBrainVLA synergizes a frozen "Left Brain", which retains robust general visual reasoning, with a trainable "Right Brain", specialized for embodied perception, via a novel Asymmetric Mixture-of-Transformers (AsyMoT) mechanism. This design allows the Right Brain to dynamically query semantic knowledge from the frozen Left Brain and fuse it with proprioceptive states, providing rich conditioning for a Flow-Matching Action Expert to generate precise continuous controls. Extensive experiments on SimplerEnv and RoboCasa benchmarks demonstrate that TwinBrainVLA achieves superior manipulation performance compared to state-of-the-art baselines while explicitly preserving the comprehensive visual understanding capabilities of the pre-trained VLM, offering a promising direction for building general-purpose robots that simultaneously achieve high-level semantic understanding and low-level physical dexterity.


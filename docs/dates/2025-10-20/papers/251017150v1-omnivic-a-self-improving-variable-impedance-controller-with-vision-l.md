---
layout: default
title: OmniVIC: A Self-Improving Variable Impedance Controller with Vision-Language In-Context Learning for Safe Robotic Manipulation
---

# OmniVIC: A Self-Improving Variable Impedance Controller with Vision-Language In-Context Learning for Safe Robotic Manipulation
**arXiv**：[2510.17150v1](https://arxiv.org/abs/2510.17150) · [PDF](https://arxiv.org/pdf/2510.17150.pdf)  
**作者**：Heng Zhang, Wei-Hsing Huang, Gokhan Solak, Arash Ajoudani  

**一句话要点**：提出OmniVIC可变阻抗控制器，结合视觉语言模型提升安全机器人操作通用性

**关键词**：可变阻抗控制, 视觉语言模型, 检索增强生成, 上下文学习, 安全机器人操作, 自适应控制

## 3 点简述
- 传统可变阻抗控制器在未知复杂任务中泛化能力不足，影响安全交互
- 采用检索增强生成和上下文学习，从图像和语言推理生成自适应阻抗参数
- 实验显示平均成功率从27%提升至61.4%，减少力违规，验证通用性

## 摘要（原文）

> We present OmniVIC, a universal variable impedance controller (VIC) enhanced
> by a vision language model (VLM), which improves safety and adaptation in any
> contact-rich robotic manipulation task to enhance safe physical interaction.
> Traditional VIC have shown advantages when the robot physically interacts with
> the environment, but lack generalization in unseen, complex, and unstructured
> safe interactions in universal task scenarios involving contact or uncertainty.
> To this end, the proposed OmniVIC interprets task context derived reasoning
> from images and natural language and generates adaptive impedance parameters
> for a VIC controller. Specifically, the core of OmniVIC is a self-improving
> Retrieval-Augmented Generation(RAG) and in-context learning (ICL), where RAG
> retrieves relevant prior experiences from a structured memory bank to inform
> the controller about similar past tasks, and ICL leverages these retrieved
> examples and the prompt of current task to query the VLM for generating
> context-aware and adaptive impedance parameters for the current manipulation
> scenario. Therefore, a self-improved RAG and ICL guarantee OmniVIC works in
> universal task scenarios. The impedance parameter regulation is further
> informed by real-time force/torque feedback to ensure interaction forces remain
> within safe thresholds. We demonstrate that our method outperforms baselines on
> a suite of complex contact-rich tasks, both in simulation and on real-world
> robotic tasks, with improved success rates and reduced force violations.
> OmniVIC takes a step towards bridging high-level semantic reasoning and
> low-level compliant control, enabling safer and more generalizable
> manipulation. Overall, the average success rate increases from 27% (baseline)
> to 61.4% (OmniVIC).


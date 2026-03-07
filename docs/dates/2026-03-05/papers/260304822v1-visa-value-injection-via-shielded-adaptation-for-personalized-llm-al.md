---
layout: default
title: VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment
---

# VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment
**arXiv**：[2603.04822v1](https://arxiv.org/abs/2603.04822) · [PDF](https://arxiv.org/pdf/2603.04822.pdf)  
**作者**：Jiawei Chen, Tianzhuo Yang, Guoxi Zhang, Jiaming Ji, Yaodong Yang, Juntao Dai  

**一句话要点**：提出VISA框架以解决大语言模型个性化对齐中的价值漂移与语义损失问题

**关键词**：大语言模型对齐, 价值注入, 闭环框架, GRPO优化, 语义完整性, 个性化价值控制

## 3 点简述
- 现有RLHF等方法仅处理粗粒度价值对齐，微调会导致价值系统漂移和语义信息损失
- VISA采用闭环架构，包含价值检测器、语义-价值转换器和基于GRPO训练的价值重写器
- 实验表明VISA在保持事实一致性和通用能力的同时，显著优于标准微调和提示方法

## 摘要（原文）

> Aligning Large Language Models (LLMs) with nuanced human values remains a critical challenge, as existing methods like Reinforcement Learning from Human Feedback (RLHF) often handle only coarse-grained attributes. In practice, fine-tuning LLMs on task-specific datasets to optimize value alignment inevitably incurs an alignment tax: the model's pre-calibrated value system drifts significantly due to latent bias absorption from training data, while the fine-tuning process also causes severe hallucinations and semantic information loss in generated responses. To address this, we propose VISA (Value Injection via Shielded Adaptation), a closed-loop framework designed to navigate this trade-off. VISA's architecture features a high-precision value detector, a semantic-to-value translator, and a core value-rewriter. The value-rewriter is trained via Group Relative Policy Optimization (GRPO) with a composite reward function that simultaneously optimizes for fine-grained value precision, and the preservation of semantic integrity. By learning an optimal policy to balance these competing objectives, VISA effectively mitigates the alignment tax while staying loyal to the original knowledge. Our experiments demonstrate that this approach enables precise control over a model's value expression while maintaining its factual consistency and general capabilities, significantly outperforming both standard fine-tuning methods and prompting-based baselines, including GPT-4o.


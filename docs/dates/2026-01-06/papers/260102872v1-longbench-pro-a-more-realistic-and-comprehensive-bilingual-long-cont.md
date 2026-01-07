---
layout: default
title: LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark
---

# LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark
**arXiv**：[2601.02872v1](https://arxiv.org/abs/2601.02872) · [PDF](https://arxiv.org/pdf/2601.02872.pdf)  
**作者**：Ziyang Chen, Xing Wu, Junlong Jia, Chaochen Gao, Qi Fu, Debing Zhang, Songlin Hu  

**一句话要点**：提出LongBench Pro双语长上下文评测基准，以更真实全面地评估大语言模型的长上下文理解能力。

**关键词**：长上下文评测, 双语基准, 人机协作构建, 上下文长度分析, 大语言模型评估

## 3 点简述
- 现有长上下文评测基准在可扩展性和真实性间存在权衡，难以覆盖真实世界复杂场景。
- 采用人机协作构建流程，结合前沿大模型生成与专家验证，平衡质量与可扩展性。
- 评估46个模型发现，长上下文优化比参数缩放更重要，且有效上下文长度常短于宣称值。

## 摘要（原文）

> The rapid expansion of context length in large language models (LLMs) has outpaced existing evaluation benchmarks. Current long-context benchmarks often trade off scalability and realism: synthetic tasks underrepresent real-world complexity, while fully manual annotation is costly to scale to extreme lengths and diverse scenarios. We present LongBench Pro, a more realistic and comprehensive bilingual benchmark of 1,500 naturally occurring long-context samples in English and Chinese spanning 11 primary tasks and 25 secondary tasks, with input lengths from 8k to 256k tokens. LongBench Pro supports fine-grained analysis with task-specific metrics and a multi-dimensional taxonomy of context requirement (full vs. partial dependency), length (six levels), and difficulty (four levels calibrated by model performance). To balance quality with scalability, we propose a Human-Model Collaborative Construction pipeline: frontier LLMs draft challenging questions and reference answers, along with design rationales and solution processes, to reduce the cost of expert verification. Experts then rigorously validate correctness and refine problematic cases. Evaluating 46 widely used long-context LLMs on LongBench Pro yields three findings: (1) long-context optimization contributes more to long-context comprehension than parameter scaling; (2) effective context length is typically shorter than the claimed context length, with pronounced cross-lingual misalignment; and (3) the "thinking" paradigm helps primarily models trained with native reasoning, while mixed-thinking designs offer a promising Pareto trade-off. In summary, LongBench Pro provides a robust testbed for advancing long-context understanding.


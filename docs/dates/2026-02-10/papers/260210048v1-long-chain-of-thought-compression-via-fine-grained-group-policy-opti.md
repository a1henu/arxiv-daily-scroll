---
layout: default
title: Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization
---

# Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization
**arXiv**：[2602.10048v1](https://arxiv.org/abs/2602.10048) · [PDF](https://arxiv.org/pdf/2602.10048.pdf)  
**作者**：Xinchen Han, Hossam Afifi, Michel Marot, Xilu Wang, Lu Yin  

**一句话要点**：提出细粒度组策略优化以压缩大语言模型中的长推理链，降低计算成本

**关键词**：推理链压缩, 强化学习优化, 细粒度策略, 大语言模型, 计算效率

## 3 点简述
- 大语言模型生成冗长推理链，增加计算开销且性能提升有限
- FGO通过细粒度分组和基于长度与熵的权重分配，实现高效推理链压缩
- 在多个推理基准上验证FGO能压缩推理链而不降低性能，并解决GRPO的局限性

## 摘要（原文）

> Large Language Models (LLMs) often generate unnecessarily verbose Chain-of-Thought (CoT) reasoning that increases computational costs and latency without proportional performance gains. In this paper, we propose \textbf{F}ine-grained \textbf{G}roup policy \textbf{O}ptimization (\textbf{FGO}), a Reinforcement Learning (RL) algorithm that refines group responses by subdividing them and assigning appropriate weights based on length and entropy, thereby enabling effective CoT compression. Meanwhile, as an enhanced variant of Group Relative Policy Optimization (GRPO), FGO successfully addresses two major limitations of the GRPO: inefficient data utilization and entropy collapse. We evaluate FGO on multiple reasoning LLMs and benchmarks, including MATH500, AIME24, AMC23, and Minerva. Experimental results show that FGO achieves efficient CoT compression without degrading performance, and simultaneously resolves the key limitations of GRPO.


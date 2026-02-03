---
layout: default
title: Self-Consolidation for Self-Evolving Agents
---

# Self-Consolidation for Self-Evolving Agents
**arXiv**：[2602.01966v1](https://arxiv.org/abs/2602.01966) · [PDF](https://arxiv.org/pdf/2602.01966.pdf)  
**作者**：Hongzhuo Yu, Fei Zhu, Guo-Sen Xie, Ling Shao  

**一句话要点**：提出自巩固框架以解决LLM智能体在长期演化中忽略失败经验和文本噪声的问题

**关键词**：LLM智能体, 自演化, 对比反思, 自巩固, 经验蒸馏, 长期学习

## 3 点简述
- 核心问题：现有LLM智能体静态运行，依赖成功轨迹检索，忽略失败经验且文本积累导致噪声和效率低下
- 方法要点：引入对比反思策略总结错误模式，并设计自巩固机制将文本经验蒸馏为紧凑可学习参数
- 实验或效果：广泛实验验证了该方法在长期智能体演化中的优势，提升性能和效率

## 摘要（原文）

> While large language model (LLM) agents have demonstrated impressive problem-solving capabilities, they typically operate as static systems, lacking the ability to evolve through lifelong interaction. Existing attempts to bridge this gap primarily rely on retrieving successful past trajectories as demonstrations. However, this paradigm faces two critical limitations. First, by focusing solely on success, agents overlook the rich pedagogical value embedded in failed attempts, preventing them from identifying and avoiding recurrent pitfalls. Second, continually accumulating textual experiences not only increases the time consumption during retrieval but also inevitably introduces noise and exhausts the largest context window of current LLMs. To address these challenges, we propose a novel self-evolving framework for LLM agents that introduces a complementary evolution mechanism: First, a contrastive reflection strategy is introduced to explicitly summarize error-prone patterns and capture reusable insights. Second, we propose a self-consolidation mechanism that distills non-parametric textual experience into compact learnable parameters. This enables the agent to internalize extensive historical experience directly into its latent space. Extensive experiments demonstrate the advantages of our method in long-term agent evolution.


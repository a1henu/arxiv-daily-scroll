---
layout: default
title: \$OneMillion-Bench: How Far are Language Agents from Human Experts?
---

# \$OneMillion-Bench: How Far are Language Agents from Human Experts?
**arXiv**：[2603.07980v1](https://arxiv.org/abs/2603.07980) · [PDF](https://arxiv.org/pdf/2603.07980.pdf)  
**作者**：Qianyu Yang, Yang Liu, Jiaqi Li, Jun Bai, Hao Chen, Kaiyuan Chen, Tiliang Duan, Jiayun Dong, Xiaobo Hu, Zixia Jia, Yang Liu, Tao Peng, Yixin Ren, Ran Tian, Zaiyuan Wang, Yanglihong Xiao, Gang Yao, Lingyue Yin, Ge Zhang, Chun Zhang, Jianpeng Jiao, Zilong Zheng, Yuan Gong  

**一句话要点**：提出OneMillion-Bench基准，评估语言代理在专业领域场景中的能力

**关键词**：语言代理评估, 专业领域基准, 多步推理, 工具使用, 权威检索, 约束决策

## 3 点简述
- 核心问题：现有基准局限于结构化任务，无法满足真实世界专业需求
- 方法要点：构建400个专家策划任务，覆盖法律、金融等行业，强调权威检索和约束决策
- 实验或效果：采用基于量规的评估协议，评分事实准确性、逻辑连贯性等维度

## 摘要（原文）

> As language models (LMs) evolve from chat assistants to long-horizon agents capable of multi-step reasoning and tool use, existing benchmarks remain largely confined to structured or exam-style tasks that fall short of real-world professional demands. To this end, we introduce \$OneMillion-Bench \$OneMillion-Bench, a benchmark of 400 expert-curated tasks spanning Law, Finance, Industry, Healthcare, and Natural Science, built to evaluate agents across economically consequential scenarios. Unlike prior work, the benchmark requires retrieving authoritative sources, resolving conflicting evidence, applying domain-specific rules, and making constraint decisions, where correctness depends as much on the reasoning process as the final answer. We adopt a rubric-based evaluation protocol scoring factual accuracy, logical coherence, practical feasibility, and professional compliance, focused on expert-level problems to ensure meaningful differentiation across agents. Together, \$OneMillion-Bench provides a unified testbed for assessing agentic reliability, professional depth, and practical readiness in domain-intensive scenarios.


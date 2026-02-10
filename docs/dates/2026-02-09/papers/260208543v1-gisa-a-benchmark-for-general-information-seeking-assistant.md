---
layout: default
title: GISA: A Benchmark for General Information-Seeking Assistant
---

# GISA: A Benchmark for General Information-Seeking Assistant
**arXiv**：[2602.08543v1](https://arxiv.org/abs/2602.08543) · [PDF](https://arxiv.org/pdf/2602.08543.pdf)  
**作者**：Yutao Zhu, Xingshuo Zhang, Maosen Zhang, Jiajie Jin, Liancheng Zhang, Xiaoshuai Song, Kangzhi Zhao, Wencong Zeng, Ruiming Tang, Han Li, Ji-Rong Wen, Zhicheng Dou  

**一句话要点**：提出GISA基准以评估通用信息搜索助手，解决现有基准不自然、任务单一和易受数据污染问题。

**关键词**：信息搜索助手, 基准评估, 结构化答案, 搜索轨迹, 数据污染, 多任务整合

## 3 点简述
- 现有基准通过反向构建查询导致任务不自然，且聚焦单一信息定位或聚合，依赖静态答案集易受数据污染。
- GISA包含373个人工构建查询，支持四种结构化答案格式，整合深度推理与广泛信息聚合，并提供完整人类搜索轨迹。
- 实验显示主流模型在GISA上表现不佳，最佳模型精确匹配率仅19.30%，尤其在复杂规划和综合信息收集任务中性能下降显著。

## 摘要（原文）

> The advancement of large language models (LLMs) has significantly accelerated the development of search agents capable of autonomously gathering information through multi-turn web interactions. Various benchmarks have been proposed to evaluate such agents. However, existing benchmarks often construct queries backward from answers, producing unnatural tasks misaligned with real-world needs. Moreover, these benchmarks tend to focus on either locating specific information or aggregating information from multiple sources, while relying on static answer sets prone to data contamination. To bridge these gaps, we introduce GISA, a benchmark for General Information-Seeking Assistants comprising 373 human-crafted queries that reflect authentic information-seeking scenarios. GISA features four structured answer formats (item, set, list, and table), enabling deterministic evaluation. It integrates both deep reasoning and broad information aggregation within unified tasks, and includes a live subset with periodically updated answers to resist memorization. Notably, GISA provides complete human search trajectories for every query, offering gold-standard references for process-level supervision and imitation learning. Experiments on mainstream LLMs and commercial search products reveal that even the best-performing model achieves only 19.30\% exact match score, with performance notably degrading on tasks requiring complex planning and comprehensive information gathering. These findings highlight substantial room for future improvement.


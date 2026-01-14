---
layout: default
title: Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards
---

# Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards
**arXiv**：[2601.08778v1](https://arxiv.org/abs/2601.08778) · [PDF](https://arxiv.org/pdf/2601.08778.pdf)  
**作者**：Tengjun Jin, Yoojin Choi, Yuxuan Zhu, Daniel Kang  

**一句话要点**：揭示文本到SQL基准中普遍标注错误对性能评估与排行榜的显著影响

**关键词**：文本到SQL, 基准评估, 标注错误, 排行榜分析, 数据质量

## 3 点简述
- 核心问题：文本到SQL基准依赖人工标注，但标注错误率高，可能误导研究与应用选择。
- 方法要点：通过专家分析量化BIRD和Spider 2.0-Snow基准的标注错误率，并修正BIRD开发集子集。
- 实验或效果：修正后代理性能变化达-7%至31%，排行榜排名变动显著，相关性分析显示错误扭曲评估结果。

## 摘要（原文）

> Researchers have proposed numerous text-to-SQL techniques to streamline data analytics and accelerate the development of database-driven applications. To compare these techniques and select the best one for deployment, the community depends on public benchmarks and their leaderboards. Since these benchmarks heavily rely on human annotations during question construction and answer evaluation, the validity of the annotations is crucial.
>   In this paper, we conduct an empirical study that (i) benchmarks annotation error rates for two widely used text-to-SQL benchmarks, BIRD and Spider 2.0-Snow, and (ii) corrects a subset of the BIRD development (Dev) set to measure the impact of annotation errors on text-to-SQL agent performance and leaderboard rankings. Through expert analysis, we show that BIRD Mini-Dev and Spider 2.0-Snow have error rates of 52.8% and 62.8%, respectively. We re-evaluate all 16 open-source agents from the BIRD leaderboard on both the original and the corrected BIRD Dev subsets. We show that performance changes range from -7% to 31% (in relative terms) and rank changes range from $-9$ to $+9$ positions. We further assess whether these impacts generalize to the full BIRD Dev set. We find that the rankings of agents on the uncorrected subset correlate strongly with those on the full Dev set (Spearman's $r_s$=0.85, $p$=3.26e-5), whereas they correlate weakly with those on the corrected subset (Spearman's $r_s$=0.32, $p$=0.23). These findings show that annotation errors can significantly distort reported performance and rankings, potentially misguiding research directions or deployment choices. Our code and data are available at https://github.com/uiuc-kang-lab/text_to_sql_benchmarks.


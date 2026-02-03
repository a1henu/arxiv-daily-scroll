---
layout: default
title: AICD Bench: A Challenging Benchmark for AI-Generated Code Detection
---

# AICD Bench: A Challenging Benchmark for AI-Generated Code Detection
**arXiv**：[2602.02079v1](https://arxiv.org/abs/2602.02079) · [PDF](https://arxiv.org/pdf/2602.02079.pdf)  
**作者**：Daniil Orel, Dilshod Azizov, Indraneil Paul, Yuxia Wang, Iryna Gurevych, Preslav Nakov  

**一句话要点**：提出AICD Bench基准以解决AI生成代码检测在分布偏移和细粒度分类中的挑战

**关键词**：AI生成代码检测, 基准测试, 分布偏移, 模型家族归因, 细粒度分类

## 3 点简述
- 核心问题：现有AI生成代码检测数据集狭窄，缺乏分布偏移和细粒度分类评估
- 方法要点：构建包含2M示例、77模型、9语言的综合基准，引入三个现实检测任务
- 实验或效果：评估显示现有检测器性能远低于实用水平，尤其在分布偏移和混合代码场景

## 摘要（原文）

> Large language models (LLMs) are increasingly capable of generating functional source code, raising concerns about authorship, accountability, and security. While detecting AI-generated code is critical, existing datasets and benchmarks are narrow, typically limited to binary human-machine classification under in-distribution settings. To bridge this gap, we introduce $\emph{AICD Bench}$, the most comprehensive benchmark for AI-generated code detection. It spans $\emph{2M examples}$, $\emph{77 models}$ across $\emph{11 families}$, and $\emph{9 programming languages}$, including recent reasoning models. Beyond scale, AICD Bench introduces three realistic detection tasks: ($\emph{i}$)~$\emph{Robust Binary Classification}$ under distribution shifts in language and domain, ($\emph{ii}$)~$\emph{Model Family Attribution}$, grouping generators by architectural lineage, and ($\emph{iii}$)~$\emph{Fine-Grained Human-Machine Classification}$ across human, machine, hybrid, and adversarial code. Extensive evaluation on neural and classical detectors shows that performance remains far below practical usability, particularly under distribution shift and for hybrid or adversarial code. We release AICD Bench as a $\emph{unified, challenging evaluation suite}$ to drive the next generation of robust approaches for AI-generated code detection. The data and the code are available at https://huggingface.co/AICD-bench}.


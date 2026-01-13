---
layout: default
title: Defenses Against Prompt Attacks Learn Surface Heuristics
---

# Defenses Against Prompt Attacks Learn Surface Heuristics
**arXiv**：[2601.07185v1](https://arxiv.org/abs/2601.07185) · [PDF](https://arxiv.org/pdf/2601.07185.pdf)  
**作者**：Shawn Li, Chenxiao Yu, Zhiyu Ni, Hao Li, Charith Peris, Chaowei Xiao, Yue Zhao  

**一句话要点**：揭示基于监督微调的提示攻击防御依赖表面启发式，导致系统误拒安全输入

**关键词**：提示攻击防御, 监督微调, 表面启发式, 误拒分析, LLM安全, 诊断数据集

## 3 点简述
- 核心问题：当前LLM提示攻击防御依赖监督微调，易学习数据中的表面相关性而非有害意图，导致误拒安全输入。
- 方法要点：分析三种防御微调诱导的捷径行为：位置偏差、令牌触发偏差和主题泛化偏差，使用诊断数据集评估。
- 实验或效果：在推理基准中，后缀任务误拒率从低于10%升至高达90%，插入触发令牌使误拒增加达50%，测试准确率下降达40%。

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed in security-sensitive applications, where they must follow system- or developer-specified instructions that define the intended task behavior, while completing benign user requests. When adversarial instructions appear in user queries or externally retrieved content, models may override intended logic. Recent defenses rely on supervised fine-tuning with benign and malicious labels. Although these methods achieve high attack rejection rates, we find that they rely on narrow correlations in defense data rather than harmful intent, leading to systematic rejection of safe inputs. We analyze three recurring shortcut behaviors induced by defense fine-tuning. \emph{Position bias} arises when benign content placed later in a prompt is rejected at much higher rates; across reasoning benchmarks, suffix-task rejection rises from below \textbf{10\%} to as high as \textbf{90\%}. \emph{Token trigger bias} occurs when strings common in attack data raise rejection probability even in benign contexts; inserting a single trigger token increases false refusals by up to \textbf{50\%}. \emph{Topic generalization bias} reflects poor generalization beyond the defense data distribution, with defended models suffering test-time accuracy drops of up to \textbf{40\%}. These findings suggest that current prompt-injection defenses frequently respond to attack-like surface patterns rather than the underlying intent. We introduce controlled diagnostic datasets and a systematic evaluation across two base models and multiple defense pipelines, highlighting limitations of supervised fine-tuning for reliable LLM security.


---
layout: default
title: This human study did not involve human subjects: Validating LLM simulations as behavioral evidence
---

# This human study did not involve human subjects: Validating LLM simulations as behavioral evidence
**arXiv**：[2602.15785v1](https://arxiv.org/abs/2602.15785) · [PDF](https://arxiv.org/pdf/2602.15785.pdf)  
**作者**：Jessica Hullman, David Broska, Huaman Sun, Aaron Shaw  

**一句话要点**：对比启发式与统计校准策略，以验证大语言模型在社会科学实验中的行为推断有效性

**关键词**：大语言模型, 社会科学实验, 合成参与者, 因果推断, 统计校准, 行为模拟

## 3 点简述
- 核心问题：大语言模型作为合成参与者在社会科学实验中的行为推断有效性缺乏明确指导
- 方法要点：对比启发式策略（如提示工程）与统计校准策略（结合辅助人类数据）
- 实验或效果：统计校准在明确假设下能保持有效性并提供更精确的因果效应估计

## 摘要（原文）

> A growing literature uses large language models (LLMs) as synthetic participants to generate cost-effective and nearly instantaneous responses in social science experiments. However, there is limited guidance on when such simulations support valid inference about human behavior. We contrast two strategies for obtaining valid estimates of causal effects and clarify the assumptions under which each is suitable for exploratory versus confirmatory research. Heuristic approaches seek to establish that simulated and observed human behavior are interchangeable through prompt engineering, model fine-tuning, and other repair strategies designed to reduce LLM-induced inaccuracies. While useful for many exploratory tasks, heuristic approaches lack the formal statistical guarantees typically required for confirmatory research. In contrast, statistical calibration combines auxiliary human data with statistical adjustments to account for discrepancies between observed and simulated responses. Under explicit assumptions, statistical calibration preserves validity and provides more precise estimates of causal effects at lower cost than experiments that rely solely on human participants. Yet the potential of both approaches depends on how well LLMs approximate the relevant populations. We consider what opportunities are overlooked when researchers focus myopically on substituting LLMs for human participants in a study.


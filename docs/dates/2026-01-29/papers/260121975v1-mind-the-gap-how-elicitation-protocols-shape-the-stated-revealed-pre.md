---
layout: default
title: Mind the Gap: How Elicitation Protocols Shape the Stated-Revealed Preference Gap in Language Models
---

# Mind the Gap: How Elicitation Protocols Shape the Stated-Revealed Preference Gap in Language Models
**arXiv**：[2601.21975v1](https://arxiv.org/abs/2601.21975) · [PDF](https://arxiv.org/pdf/2601.21975.pdf)  
**作者**：Pranav Mahajan, Ihor Kendiukhov, Syed Hussain, Lydia Nottingham  

**一句话要点**：研究提示协议如何影响语言模型的陈述-揭示偏好差距，提出考虑不确定偏好的方法

**关键词**：语言模型偏好, 陈述-揭示偏好差距, 提示协议, 偏好诱导, 相关性分析, 中立偏好

## 3 点简述
- 核心问题：语言模型存在陈述-揭示偏好差距，现有评估方法混淆了真实偏好与提示协议的人为因素
- 方法要点：系统研究24个语言模型，通过允许中立和弃权来改进陈述偏好与揭示偏好的相关性
- 实验或效果：发现相关性高度依赖协议，陈述偏好引导在揭示偏好中未可靠改善相关性

## 摘要（原文）

> Recent work identifies a stated-revealed (SvR) preference gap in language models (LMs): a mismatch between the values models endorse and the choices they make in context. Existing evaluations rely heavily on binary forced-choice prompting, which entangles genuine preferences with artifacts of the elicitation protocol. We systematically study how elicitation protocols affect SvR correlation across 24 LMs. Allowing neutrality and abstention during stated preference elicitation allows us to exclude weak signals, substantially improving Spearman's rank correlation ($ρ$) between volunteered stated preferences and forced-choice revealed preferences. However, further allowing abstention in revealed preferences drives $ρ$ to near-zero or negative values due to high neutrality rates. Finally, we find that system prompt steering using stated preferences during revealed preference elicitation does not reliably improve SvR correlation on AIRiskDilemmas. Together, our results show that SvR correlation is highly protocol-dependent and that preference elicitation requires methods that account for indeterminate preferences.


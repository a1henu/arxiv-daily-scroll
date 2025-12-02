---
layout: default
title: First, do NOHARM: towards clinically safe large language models
---

# First, do NOHARM: towards clinically safe large language models
**arXiv**：[2512.01241v1](https://arxiv.org/abs/2512.01241) · [PDF](https://arxiv.org/pdf/2512.01241.pdf)  
**作者**：David Wu, Fateme Nateghi Haredasht, Saloni Kumar Maharaj, Priyank Jain, Jessica Tran, Matthew Gwiazdon, Arjun Rustagi, Jenelle Jindal, Jacob M. Koshy, Vinay Kadiyala, Anup Agarwal, Bassman Tappuni, Brianna French, Sirus Jesudasen, Christopher V. Cosgriff, Rebanta Chakraborty, Jillian Caldwell, Susan Ziolkowski, David J. Iberri, Robert Diep, Rahul S. Dalal, Kira L. Newman, Kristin Galetta, J. Carl Pallais, Nancy Wei, Kathleen M. Buchheit, David I. Hong, Ernest Y. Lee, Allen Shih, Vartan Pahalyants, Tamara B. Kaplan, Vishnu Ravi, Sarita Khemani, April S. Liang, Daniel Shirvani, Advait Patil, Nicholas Marshall, Kanav Chopra, Joel Koh, Adi Badhwar, Liam G. McCoy, David J. H. Wu, Yingjie Weng, Sumant Ranji, Kevin Schulman, Nigam H. Shah, Jason Hom, Arnold Milstein, Adam Rodman, Jonathan H. Chen, Ethan Goh  

**一句话要点**：提出NOHARM基准以评估大语言模型在医疗咨询中的临床安全性

**关键词**：大语言模型, 临床安全性评估, 医疗咨询基准, 危害分析, 多智能体系统

## 3 点简述
- 核心问题：大语言模型在医疗建议中的临床安全性未充分评估，存在潜在危害风险。
- 方法要点：基于100个真实初级到专科咨询案例，构建NOHARM基准，涵盖10个专科，通过专家标注量化危害频率与严重性。
- 实验或效果：在31个模型中，严重危害率高达22.2%，遗漏危害占错误76.6%，安全性能与现有基准相关性中等，多智能体方法可降低危害。

## 摘要（原文）

> Large language models (LLMs) are routinely used by physicians and patients for medical advice, yet their clinical safety profiles remain poorly characterized. We present NOHARM (Numerous Options Harm Assessment for Risk in Medicine), a benchmark using 100 real primary-care-to-specialist consultation cases to measure harm frequency and severity from LLM-generated medical recommendations. NOHARM covers 10 specialties, with 12,747 expert annotations for 4,249 clinical management options. Across 31 LLMs, severe harm occurs in up to 22.2% (95% CI 21.6-22.8%) of cases, with harms of omission accounting for 76.6% (95% CI 76.4-76.8%) of errors. Safety performance is only moderately correlated (r = 0.61-0.64) with existing AI and medical knowledge benchmarks. The best models outperform generalist physicians on safety (mean difference 9.7%, 95% CI 7.0-12.5%), and a diverse multi-agent approach reduces harm compared to solo models (mean difference 8.0%, 95% CI 4.0-12.1%). Therefore, despite strong performance on existing evaluations, widely used AI models can produce severely harmful medical advice at nontrivial rates, underscoring clinical safety as a distinct performance dimension necessitating explicit measurement.


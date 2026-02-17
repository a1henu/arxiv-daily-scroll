---
layout: default
title: Hunt Globally: Deep Research AI Agents for Drug Asset Scouting in Investing, Business Development, and Search & Evaluation
---

# Hunt Globally: Deep Research AI Agents for Drug Asset Scouting in Investing, Business Development, and Search & Evaluation
**arXiv**：[2602.15019v1](https://arxiv.org/abs/2602.15019) · [PDF](https://arxiv.org/pdf/2602.15019.pdf)  
**作者**：Alisa Vinogradova, Vlad Vinogradov, Luba Greenwood, Ilya Yasny, Dmitry Kobyzev, Shoman Kasbekar, Kong Nguyen, Dmitrii Radkevich, Roman Doronin, Andrey Doronichev  

**一句话要点**：提出树状自学习Bioptic Agent与基准方法，用于多语言药物资产侦察，以提升覆盖完整性与减少幻觉。

**关键词**：药物资产侦察, 多语言信息检索, AI基准测试, 树状自学习代理, 幻觉减少, 投资与业务开发

## 3 点简述
- 核心问题：当前深度研究AI代理在多语言异构源中实现高召回发现时仍落后于人类专家，存在幻觉风险。
- 方法要点：设计基于树的自我学习Bioptic Agent，构建多语言多代理管道基准，使用LLM作为评判器进行校准评估。
- 实验或效果：Bioptic Agent在基准测试中达到79.7% F1分数，优于其他主流AI模型，性能随计算资源增加而提升。

## 摘要（原文）

> Bio-pharmaceutical innovation has shifted: many new drug assets now originate outside the United States and are disclosed primarily via regional, non-English channels. Recent data suggests >85% of patent filings originate outside the U.S., with China accounting for nearly half of the global total; a growing share of scholarly output is also non-U.S. Industry estimates put China at ~30% of global drug development, spanning 1,200+ novel candidates. In this high-stakes environment, failing to surface "under-the-radar" assets creates multi-billion-dollar risk for investors and business development teams, making asset scouting a coverage-critical competition where speed and completeness drive value. Yet today's Deep Research AI agents still lag human experts in achieving high-recall discovery across heterogeneous, multilingual sources without hallucinations.
>   We propose a benchmarking methodology for drug asset scouting and a tuned, tree-based self-learning Bioptic Agent aimed at complete, non-hallucinated scouting. We construct a challenging completeness benchmark using a multilingual multi-agent pipeline: complex user queries paired with ground-truth assets that are largely outside U.S.-centric radar. To reflect real deal complexity, we collected screening queries from expert investors, BD, and VC professionals and used them as priors to conditionally generate benchmark queries. For grading, we use LLM-as-judge evaluation calibrated to expert opinions. We compare Bioptic Agent against Claude Opus 4.6, OpenAI GPT-5.2 Pro, Perplexity Deep Research, Gemini 3 Pro + Deep Research, and Exa Websets. Bioptic Agent achieves 79.7% F1 versus 56.2% (Claude Opus 4.6), 50.6% (Gemini 3 Pro + Deep Research), 46.6% (GPT-5.2 Pro), 44.2% (Perplexity Deep Research), and 26.9% (Exa Websets). Performance improves steeply with additional compute, supporting the view that more compute yields better results.


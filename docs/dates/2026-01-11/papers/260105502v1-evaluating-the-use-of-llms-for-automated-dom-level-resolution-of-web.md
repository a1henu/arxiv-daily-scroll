---
layout: default
title: Evaluating the Use of LLMs for Automated DOM-Level Resolution of Web Performance Issues
---

# Evaluating the Use of LLMs for Automated DOM-Level Resolution of Web Performance Issues
**arXiv**：[2601.05502v1](https://arxiv.org/abs/2601.05502) · [PDF](https://arxiv.org/pdf/2601.05502.pdf)  
**作者**：Gideon Peters, SayedHassan Khatoonabadi, Emad Shihab  

**一句话要点**：评估LLMs在自动化DOM级网页性能问题解决中的应用效果

**关键词**：大型语言模型, 网页性能优化, DOM操作, 自动化审计, Lighthouse工具, 性能评估

## 3 点简述
- 核心问题：网页性能优化中DOM修改复杂耗时，需自动化解决方案。
- 方法要点：提取15个流行网页的DOM树和Lighthouse审计报告，测试9个先进LLMs的解决能力。
- 实验或效果：LLMs在SEO与可访问性方面表现优异，但性能关键DOM操作效果不一，如GPT-4.1显著减少审计发生率，而GPT-4o-mini表现不佳。

## 摘要（原文）

> Users demand fast, seamless webpage experiences, yet developers often struggle to meet these expectations within tight constraints. Performance optimization, while critical, is a time-consuming and often manual process. One of the most complex tasks in this domain is modifying the Document Object Model (DOM), which is why this study focuses on it. Recent advances in Large Language Models (LLMs) offer a promising avenue to automate this complex task, potentially transforming how developers address web performance issues. This study evaluates the effectiveness of nine state-of-the-art LLMs for automated web performance issue resolution. For this purpose, we first extracted the DOM trees of 15 popular webpages (e.g., Facebook), and then we used Lighthouse to retrieve their performance audit reports. Subsequently, we passed the extracted DOM trees and corresponding audits to each model for resolution. Our study considers 7 unique audit categories, revealing that LLMs universally excel at SEO & Accessibility issues. However, their efficacy in performance-critical DOM manipulations is mixed. While high-performing models like GPT-4.1 delivered significant reductions in areas like Initial Load, Interactivity, and Network Optimization (e.g., 46.52% to 48.68% audit incidence reductions), others, such as GPT-4o-mini, notably underperformed, consistently. A further analysis of these modifications showed a predominant additive strategy and frequent positional changes, alongside regressions particularly impacting Visual Stability.

